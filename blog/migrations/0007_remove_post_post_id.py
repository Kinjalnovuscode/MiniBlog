# Generated by Django 5.1.5 on 2025-01-27 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_id',
        ),
    ]
