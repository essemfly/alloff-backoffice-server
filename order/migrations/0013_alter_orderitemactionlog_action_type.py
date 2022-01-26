# Generated by Django 3.2.8 on 2022-01-25 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_alter_orderitemactionlog_action_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitemactionlog',
            name='action_type',
            field=models.CharField(choices=[('STATUS_CHANGE', 'Status Change'), ('MEMO_ADD', 'Memo Add'), ('MEMO_DELETE', 'Memo Delete'), ('PAYMENT_ADJUSTMENT', 'Payment Adjustment'), ('REFUND_UPDATE', 'Refund Update'), ('RECEIVED_ITEM', 'Received Item'), ('FORCE_RECEIVED_ITEM', 'Force Received Item')], max_length=100),
        ),
    ]
