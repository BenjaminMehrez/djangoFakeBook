# Generated by Django 5.1 on 2024-09-10 21:18

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a_posts', '0018_alter_tag_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
