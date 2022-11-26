# Generated by Django 4.1.1 on 2022-10-06 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_merge_20221005_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('decline', 'Decline'), ('approved', 'Approved'), ('processing', 'Processing'), ('complete', 'Complete'), ('bulk', 'Bulk')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('instock', 'instock'), ('notInstock', 'notInstock')], default='', max_length=10),
        ),
    ]
