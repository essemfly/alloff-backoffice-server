from datetime import datetime

from tagger.core.mongo.models.order import OrderType
from tagger.models import Inventory, ReceivedItem
from tagger.models.inventory import InventoryStatus, ProductType


def make_inventory_with_received_item(ri: ReceivedItem) -> Inventory:
    today = datetime.now().date()
    today_inventory_count = Inventory.objects.filter(created__gte=today).count()
    code_prefix = today.isoformat()[2:].replace("-", "")
    current_sequence = today_inventory_count + 1  # 0 inventories --> current is #1 (starts with 1)
    code = f"{code_prefix}-{str(current_sequence).zfill(3)}"

    if ri.is_return:
        code += "-R"
    if ri.needs_processing:
        code += "-NP"

    return Inventory.objects.create(
        code=code,
        status=InventoryStatus.PROCESSING_NEEDED if ri.needs_processing else InventoryStatus.IN_STOCK,
        size=ri.size,
        product_id=ri.product_id,
        in_order_id=ri.order_id,
        product_name=ri.item_name,
        product_brand=ri.brand_keyname,
        product_type=ProductType.NORMAL_PRODUCT if ri.order_type == OrderType.NORMAL_ORDER else ProductType.TIMEDEAL_PRODUCT,
    )
