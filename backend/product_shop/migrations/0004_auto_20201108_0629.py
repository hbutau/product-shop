# Generated by Django 3.1.3 on 2020-11-08 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product_shop", "0003_auto_20201107_1613"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="paid",
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
