# Generated by Django 4.1.7 on 2023-02-24 13:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_posts_delete_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="posts",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
