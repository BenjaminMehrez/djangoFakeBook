# Generated by Django 5.1.1 on 2024-10-12 03:55

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a_posts', '0003_alter_tag_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
    ]
