# Generated by Django 3.2.8 on 2021-11-08 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tagger', '0007_auto_20211108_0516'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='location',
            field=models.CharField(default='큐브', max_length=50),
            preserve_default=False,
        ),
    ]