from datetime import date

import xlwt
from protos.logistics.package.package_pb2 import Package
from protos.logistics.shipping_notice.shipping_notice_pb2 import ShippingNotice

CJ_COLUMNS = [
    "주문번호",
    "주문일",
    "수령자명",
    "수령자 우편번호",
    "수령자 연락처",
    "수령자주소",
    "상품명",
    "옵션명",
    "수량",
    "배송메모",
    "박스타입",
]


def make_cj_workbook(notice: ShippingNotice) -> xlwt.Workbook:
    wb = xlwt.Workbook()
    ws = wb.add_sheet("Sheet1")
    for col, val in enumerate(CJ_COLUMNS):
        ws.write(0, col, val)

    data = [get_cj_row(package) for package in notice.packages]
    for row, item in enumerate(data):
        for col, val in enumerate(item):
            ws.write(row + 1, col, val)
    return wb


def get_cj_row(package: Package):
    inventories = package.inventories

    item_name = inventories[0].product_name
    item_size = inventories[0].size

    item_count = len(inventories)
    if item_count > 1:
        item_name += f" 외 {item_count - 1}"
        item_size += f" 외 {item_count - 1}"

    return [
        package.code,
        date.today().isoformat().replace("-", "/"),
        package.customer_name,
        package.post_code,
        f"{package.customer_mobile[:3]}-{package.customer_mobile[3:7]}-{package.customer_mobile[7:11]}",
        package.address,
        item_name,
        item_size,
        1,
        package.delivery_note,
        "극소",
    ]
