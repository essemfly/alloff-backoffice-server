# Generated by Django 3.2.8 on 2022-02-09 15:53

from django.db import migrations, models
import office.models.company_brand


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0003_auto_20220209_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='companybrand',
            name='brand_key',
            field=models.CharField(db_index=True, default=office.models.company_brand._make_brand_key, editable=False, max_length=50, unique=True),
        ),
    ]
