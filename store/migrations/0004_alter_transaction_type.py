# Generated by Django 4.1.3 on 2024-08-01 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_transaction_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.CharField(choices=[('In', 'In'), ('Out', 'Out')], default='', max_length=20),
        ),
    ]