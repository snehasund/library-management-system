# Generated by Django 4.2.10 on 2024-03-01 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("django_project", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="book", name="quantity",),
    ]
