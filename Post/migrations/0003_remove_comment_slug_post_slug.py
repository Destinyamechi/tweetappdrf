# Generated by Django 4.2.7 on 2024-01-11 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_remove_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='slug',
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]