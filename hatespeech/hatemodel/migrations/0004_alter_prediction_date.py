# Generated by Django 5.0.6 on 2024-07-05 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hatemodel", "0003_remove_prediction_day_of_week"),
    ]

    operations = [
        migrations.AlterField(
            model_name="prediction",
            name="date",
            field=models.DateField(auto_now_add=True),
        ),
    ]