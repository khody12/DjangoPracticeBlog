# Generated by Django 4.2.14 on 2024-07-28 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Excerpt',
            new_name='excerpt',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Image_Name',
            new_name='image_Name',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Slug',
            new_name='slug',
        ),
    ]
