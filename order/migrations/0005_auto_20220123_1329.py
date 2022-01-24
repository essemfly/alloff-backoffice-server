# Generated by Django 3.2.8 on 2022-01-23 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20220123_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitemalimtalklog',
            name='order_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='alimtalk', to='order.orderitem'),
        ),
        migrations.AlterField(
            model_name='orderitemrefundupdatelog',
            name='order_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='refund_update', to='order.orderitem'),
        ),
        migrations.AlterField(
            model_name='orderitemstatuschangelog',
            name='order_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='status_change', to='order.orderitem'),
        ),
    ]
