# Generated by Django 4.2.10 on 2024-03-19 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_alter_about_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='author',
        ),
    ]
