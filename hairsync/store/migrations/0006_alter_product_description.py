# Generated by Django 5.0.7 on 2024-08-20 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0005_alter_category_options_category_slug_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(blank=True, default="Default description"),
        ),
    ]
