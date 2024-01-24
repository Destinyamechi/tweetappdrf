# Generated by Django 5.0.1 on 2024-01-13 11:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0004_qoutetweet_repost_threadtweet'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Post.comment'),
        ),
        migrations.DeleteModel(
            name='ThreadTweet',
        ),
    ]
