# Generated by Django 3.2.6 on 2021-08-05 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_auto_20210805_0925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='dislike',
            new_name='dislikes',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='like',
            new_name='likes',
        ),
    ]