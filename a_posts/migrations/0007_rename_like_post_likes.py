# Generated by Django 5.1 on 2024-08-30 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a_posts', '0006_likedpost_post_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='like',
            new_name='likes',
        ),
    ]