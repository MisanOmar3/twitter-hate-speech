# Generated by Django 5.0.6 on 2024-07-05 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hatemodel", "0006_alter_review_classification"),
    ]

    operations = [
        migrations.AddField(
            model_name="prediction",
            name="accuracy",
            field=models.CharField(default="92.22%", max_length=6),
            preserve_default=False,
        ),
    ]