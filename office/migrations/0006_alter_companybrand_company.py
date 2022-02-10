# Generated by Django 3.2.8 on 2022-02-10 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0005_alter_companybrand_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companybrand',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='company_brands', to='office.company'),
        ),
    ]
