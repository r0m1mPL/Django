# Generated by Django 4.0.3 on 2022-04-11 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_folowers_follower_followers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created_at',), 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
    ]
