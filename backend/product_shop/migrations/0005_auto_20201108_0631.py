# Generated by Django 3.1.3 on 2020-11-08 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product_shop", "0004_auto_20201108_0629"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="paid",
            field=models.BooleanField(default=False),
        ),
    ]