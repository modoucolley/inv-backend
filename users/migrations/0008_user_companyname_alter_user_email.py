# Generated by Django 4.1.3 on 2022-12-04 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_auto_20221124_1653"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="companyname",
            field=models.CharField(default="", max_length=120),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
