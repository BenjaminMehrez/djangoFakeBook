# Generated by Django 5.1.3 on 2024-11-12 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LandingPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('is_enabled', models.BooleanField(default=False)),
                ('access_code', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
