# Generated by Django 3.2.8 on 2021-11-08 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tagger', '0006_auto_20211105_0408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('MADAM', 'Madam'), ('MALL', 'Mall'), ('OFFLINE', 'Offline'), ('INVENTORY', 'Inventory')], max_length=20)),
                ('bank_name', models.CharField(max_length=20)),
                ('bank_account_holder', models.CharField(max_length=40)),
                ('bank_account_number', models.CharField(max_length=40)),
                ('biz_registration_id', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='inventory',
            name='out_order_id',
            field=models.CharField(db_index=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='status',
            field=models.CharField(choices=[('IN_STOCK', 'In Stock'), ('SHIPPED', 'Shipped'), ('SHIPPING_PENDING', 'Shipping Pending')], max_length=30),
        ),
    ]
