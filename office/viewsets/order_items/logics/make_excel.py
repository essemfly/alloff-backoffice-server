from openpyxl import Workbook
from openpyxl.writer.excel import save_virtual_workbook

_HEADER = [
    "주문번호",
    "주문순번(단건코드)",
    "주문일자",
    "쇼핑몰 상품코드",
    "상태",
    "상품명",
    "옵션명",
    "주문수량",
    "주문금액",
    "결제금액",
    "판매가",
    "주문자 ID",
    "주문자명",
    "주문자 연락처",
    "수취인명",
    "수취인 전화번호",
    "수취인 핸드폰번호",
    "수취인 주소",
    "수취인 우편번호",
    "배송비",
    "배송메세지",
]


def make_order_item_excel(grpc_order_item_stream):
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.append(_HEADER)
    for order_item in grpc_order_item_stream:
        worksheet.append(_make_row(order_item))
    return save_virtual_workbook(workbook)


def _make_row(order_item):
    return [
        order_item.order.alloff_order_id,  # 주문번호*
        order_item.order_item_code,  # 부주문번호
        order_item.ordered_at,  # 주문일자
        order_item.product_id,  # 쇼핑몰 상품코드*
        order_item.order_item_status,  # 상태
        order_item.product_name,  # 상품명*
        f"size: {order_item.size} / color: {order_item.color}",  # 옵션명*
        order_item.quantity,  # 주문수량*
        order_item.total_amount,  # 주문금액
        order_item.total_amount,  # 결제금액
        order_item.sales_price,  # 판매가*
        order_item.order.user_id,  # 주문자 ID*
        order_item.order.orderer_name,  # 주문자명*
        order_item.order.orderer_mobile,  # 주문자 연락처
        order_item.order.recipient_name,  # 수취인명*
        order_item.order.recipient_mobile,  # 수취인 전화번호*
        order_item.order.recipient_mobile,  # 수취인 핸드폰번호*
        order_item.order.recipient_address,  # 수취인 주소*
        order_item.order.recipient_postcode,  # 수취인 우편번호*
        0,  # 배송비
        order_item.order.user_memo,  # 배송메세지
    ]
