# Generated by Django 5.1.3 on 2024-11-14 18:19

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a_posts', '0006_alter_tag_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
    ]