# Generated by Django 5.1.1 on 2024-09-13 14:25

import django.db.models.deletion
import django.utils.timezone
import comelive.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("name", models.CharField(blank=True, default="", max_length=20)),
                ("is_renter", models.BooleanField(default=False)),
                ("is_landlord", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("is_superuser", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                (
                    "date_joined",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("last_login", models.DateTimeField(blank=True, null=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "ordering": ["email"],
            },
            managers=[
                ("objects", comelive.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Ad",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                ("state", models.CharField(max_length=50)),
                ("city", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=150)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("rooms", models.PositiveSmallIntegerField()),
                (
                    "type",
                    models.CharField(
                        choices=[("Apartment", "Apartment"), ("House", "House")],
                        max_length=20,
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "ad",
                "verbose_name_plural": "ads",
                "ordering": ["-id"],
            },
        ),
    ]