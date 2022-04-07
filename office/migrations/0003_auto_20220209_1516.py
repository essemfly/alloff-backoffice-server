# Generated by Django 3.2.8 on 2022-02-09 15:16

from django.db import migrations, models
import django.db.models.deletion
import office.models.api
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("office", "0002_profile_uuid"),
    ]

    operations = [
        migrations.CreateModel(
            name="ApiKey",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("ACTIVE", "Active"), ("INACTIVE", "Inactive")],
                        default="INACTIVE",
                        max_length=30,
                    ),
                ),
                (
                    "key",
                    models.CharField(
                        db_index=True,
                        default=office.models.api._make_api_key,
                        editable=False,
                        max_length=100,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "api_keys",
            },
        ),
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[("ACTIVE", "Active"), ("INACTIVE", "Inactive")],
                        default="INACTIVE",
                        max_length=10,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "api_key",
                    models.OneToOneField(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="office.apikey",
                    ),
                ),
            ],
            options={
                "db_table": "companies",
            },
        ),
        migrations.AddField(
            model_name="profile",
            name="profile_type",
            field=models.CharField(
                choices=[("ADMIN", "Admin"), ("COMPANY_USER", "Company User")],
                default="ADMIN",
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="uuid",
            field=models.UUIDField(
                db_index=True, default=uuid.uuid4, editable=False, unique=True
            ),
        ),
        migrations.AlterModelTable(
            name="profile",
            table="profiles",
        ),
        migrations.CreateModel(
            name="CompanyBrand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "brand_id",
                    models.CharField(db_index=True, max_length=24, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="office.company"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="profile",
            name="company",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="office.company",
            ),
        ),
    ]
