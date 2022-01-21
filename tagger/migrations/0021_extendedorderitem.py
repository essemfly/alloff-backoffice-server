# Generated by Django 3.2.8 on 2021-11-16 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tagger', '0020_inventory_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(choices=[('NORMAL', 'Normal Product'), ('TIMEDEAL', 'Timedeal Product')], max_length=30)),
                ('size', models.CharField(max_length=30)),
                ('quantity', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('product_code', models.CharField(db_index=True, max_length=50)),
                ('product_id', models.CharField(db_index=True, max_length=30)),
                ('brand_keyname', models.CharField(max_length=30)),
                ('eo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tagger.extendedorder')),
            ],
        ),
    ]
