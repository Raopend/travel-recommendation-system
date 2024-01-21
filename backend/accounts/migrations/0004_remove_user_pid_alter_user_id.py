# Generated by Django 5.0.1 on 2024-01-21 16:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_user_pid"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="pid",
        ),
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]