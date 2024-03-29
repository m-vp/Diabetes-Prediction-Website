# Generated by Django 4.2.7 on 2023-11-15 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Result",
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
                ("pregnancies", models.FloatField()),
                ("glucose", models.FloatField()),
                ("BP", models.FloatField()),
                ("skin_thickness", models.FloatField()),
                ("Insulin", models.FloatField()),
                ("BMI", models.FloatField()),
                ("DPF", models.FloatField()),
                ("age", models.FloatField()),
                ("result_value", models.CharField(max_length=20)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
