# Generated by Django 4.1.3 on 2023-06-02 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0011_alter_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='current_stock',
            field=models.PositiveIntegerField(default=1),
        ),
    ]