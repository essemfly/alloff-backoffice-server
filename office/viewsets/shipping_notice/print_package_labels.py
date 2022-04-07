from gen.pyalloff.package_pb2 import Package
from office.label.print_label import print_label
from office.label.shipping_label import (
    make_box_shipping_label,
    make_item_shipping_label,
)


def print_package_labels(package: Package):
    """
    Print package labels for a Package.
    """
    items_count = len(package.inventories)
    for index, inventory in enumerate(package.inventories):
        print(f"""MARKING SHIPPING PENDING - {inventory.code}""")
        if items_count > 1:
            print(
                f"""PRINTING ITEM LABEL FOR {package.code} ({package.customer_name} {package.address})"""
            )
            print_label(
                make_item_shipping_label(package, inventory, index, items_count)
            )

    print(
        f"""PRINTING BOX LABEL FOR {package.code} ({package.customer_name} {package.address})"""
    )
    print_label(make_box_shipping_label(package))
