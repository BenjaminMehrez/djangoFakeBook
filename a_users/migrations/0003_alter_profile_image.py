# Generated by Django 5.1 on 2024-09-08 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_users', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
    ]
