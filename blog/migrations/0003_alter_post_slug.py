# Generated by Django 4.2.14 on 2024-07-28 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_date_post_date_rename_excerpt_post_excerpt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
