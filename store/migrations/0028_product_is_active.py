# Generated by Django 4.1.3 on 2024-02-11 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_rename_cost_rice_product_cost_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
