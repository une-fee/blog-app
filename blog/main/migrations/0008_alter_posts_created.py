# Generated by Django 4.1.7 on 2023-02-24 15:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0007_alter_posts_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="posts",
            name="created",
            field=models.DateField(auto_now_add=True),
        ),
    ]
