from tagger.core.label.print_label import print_label
from tagger.core.label.shipping_label import make_item_shipping_label, make_box_shipping_label
from tagger.models import Package
from tagger.models.inventory import InventoryStatus
from tagger.models.package import PackageStatus


def seal_package(package: Package):
    items = package.shipping_notice_items.all()
    items_count = len(items)
    for index, item in enumerate(items):
        print(f"""MARKING SHIPPING PENDING - INV {item.inventory.code}""")
        item.inventory.status = InventoryStatus.SHIPPING_PENDING
        item.inventory.save()
        if items_count > 1:
            print(f"""PRINTING ITEM LABEL FOR {package.code} ({package.recipient_name} {package.address})""")
            print_label(make_item_shipping_label(package, item, index, items_count))

    print(f"""PRINTING BOX LABEL FOR {package.code} ({package.recipient_name} {package.address})""")
    print_label(make_box_shipping_label(package))
    package.status = PackageStatus.CREATED
    package.save()
    return package
