# Generated by Django 4.1.7 on 2023-02-24 14:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0005_alter_posts_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="posts",
            name="created",
            field=models.DateField(auto_now_add=True),
        ),
    ]