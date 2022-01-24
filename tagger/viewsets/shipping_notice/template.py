from datetime import date

import xlwt

from tagger.models import Package, ShippingNotice

CJ_COLUMNS = [
    "주문번호", "주문일", "수령자명", "수령자 우편번호", "수령자 연락처", "수령자주소", "상품명", "옵션명", "수량", "배송메모", "박스타입"
]


def make_cj_workbook(notice: ShippingNotice) -> xlwt.Workbook:
    wb = xlwt.Workbook()
    ws = wb.add_sheet("Sheet1")
    for col, val in enumerate(CJ_COLUMNS):
        ws.write(0, col, val)

    data = [get_cj_row(package) for package in notice.packages.all()]
    for row, item in enumerate(data):
        for col, val in enumerate(item):
            ws.write(row + 1, col, val)
    return wb


def get_cj_row(package: Package):
    items = package.shipping_notice_items.all()

    item_name = items[0].item.name
    item_size = items[0].item.size

    item_count = len(items)
    if item_count > 1:
        item_name += f" 외 {item_count - 1}"
        item_size += f" 외 {item_count - 1}"

    return [
        package.code,
        date.today().isoformat().replace("-", "/"),
        package.recipient_name,
        package.postcode,
        f"{package.recipient_mobile[:3]}-{package.recipient_mobile[3:7]}-{package.recipient_mobile[7:11]}",
        package.address,
        item_name,
        item_size,
        1,
        items[0].item.extended_order.order.memo,
        "소"
    ]
