# Generated by Django 5.0.6 on 2024-06-24 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
