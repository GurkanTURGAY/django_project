# Generated by Django 5.0.6 on 2024-06-26 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0007_alter_category_slug_alter_course_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='category',
        ),
        migrations.AddField(
            model_name='course',
            name='categories',
            field=models.ManyToManyField(to='djangoapp.category'),
        ),
    ]
