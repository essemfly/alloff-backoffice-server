# Generated by Django 3.2.8 on 2022-01-21 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20220121_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitemmemo',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
