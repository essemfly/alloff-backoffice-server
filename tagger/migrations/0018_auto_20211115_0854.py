# Generated by Django 3.2.8 on 2021-11-15 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tagger', '0017_receiveditem_memo'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='in_order_id',
            field=models.CharField(blank=True, db_index=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='receiveditem',
            name='inventory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tagger.inventory'),
        ),
        migrations.AlterField(
            model_name='receiveditem',
            name='processor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='receiveditem',
            name='sourcing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tagger.sourcing'),
        ),
    ]