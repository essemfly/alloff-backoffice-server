from typing import List, Dict, Tuple

from django.db.models import Q
from rest_framework import viewsets, mixins

from tagger.core.mongo.models.order import OrderStatus
from tagger.models import ExtendedOrderItem, ExtendedOrder
from tagger.models.inventory import InventoryStatus, Inventory
from tagger.models.shipping_notice import ShippingNotice, ShippingNoticeItem
from tagger.serializers.shipping import ShippingNoticeSerializer


def _get_candidate_eois(i: Inventory, exhausted_eoi_ids: set):
    # print(f"""Finding candidates for inv id {i.id} ({i.code})""")
    query = Q(product_code=i.product_code) | Q(product_type=i.product_type, product_id=i.product_id)
    print(query)
    return [x for x in ExtendedOrderItem.objects.filter(query).all()
            if x.id not in exhausted_eoi_ids
            # it's not in the query for removing whitespaces
            and "".join(x.size.split()) == "".join(i.size.split())
            and x.extended_order.order.orderstatus in [
                OrderStatus.PAYMENT_FINISHED,
                OrderStatus.PRODUCT_PREPARING,
                OrderStatus.DELIVERY_PREPARING,
                OrderStatus.CANCEL_FINISHED,
            ]]


def _pick_match_from_candidate_eois(candidate_eois: List[ExtendedOrderItem]):
    assert len(candidate_eois) > 0
    return sorted(candidate_eois, key=lambda x: x.extended_order.order.created)[0]


def _filter_fulfilled_candidates(candidates: Dict[str, Dict]) -> Dict[str, Dict]:
    return {order_id: x for order_id, x in candidates.items() if len(x["eo"].order.orders) == len(x["items"])}


def make_shipping_notice():
    from tagger.models import Inventory
    inventories = Inventory.objects.filter(
        status=InventoryStatus.IN_STOCK,
        shippingnoticeitem__isnull=True,
    ).order_by("id").all()

    candidates = {}
    exhausted_eoi_ids = set()

    for i in inventories:
        print(f"Processing inventory {i.code}")
        candidate_eois = _get_candidate_eois(i, exhausted_eoi_ids)
        if len(candidate_eois) == 0:
            print(f"""No candidates for {i.id}, moving on...""")
            continue
        else:
            match = _pick_match_from_candidate_eois(candidate_eois)
            order_id = match.extended_order.order_id
            if order_id not in candidates:
                print(f"""Order {order_id} newly being fulfilled""")
                candidates[order_id] = {
                    "eo": match.extended_order,
                    "items": []
                }
            exhausted_eoi_ids.add(match.id)
            candidates[order_id]["items"].append((i, match))
            print(f"""Order {order_id} now gets {match.product_code}""")

    # Filter only fulfilled orders
    fulfilled_candidates = _filter_fulfilled_candidates(candidates)

    # If no fulfilled_candidates, return.
    if not fulfilled_candidates:  # {} evaluates to False
        print(f"""No orders are fulfilled! Exiting...""")
        return

    notice = ShippingNotice.objects.create()
    print(f"""Shipping notice {notice.code} has been created!""")

    for candidate in fulfilled_candidates.values():
        eo = candidate["eo"]  # type: ExtendedOrder
        items = candidate["items"]  # type: List[Tuple[Inventory, ExtendedOrderItem]]

        for inventory, eoi in items:
            ShippingNoticeItem.objects.create(
                notice=notice,
                inventory=inventory,
                item=eoi
            )

    return notice


class ShippingNoticeViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = ShippingNotice.objects.order_by("-id")
    serializer_class = ShippingNoticeSerializer

    # filter_backends = [SearchFilter, DjangoFilterBackend]
    # search_fields = ['code', 'product_name', 'out_order_id', 'in_order_id']
    # filterset_class = InventoryFilter

    def list(self, request, *args, **kwargs):
        make_shipping_notice()
        return super().list(request, *args, **kwargs)
