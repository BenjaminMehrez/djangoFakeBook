# Generated by Django 5.1 on 2024-09-02 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a_posts', '0009_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created']},
        ),
    ]
