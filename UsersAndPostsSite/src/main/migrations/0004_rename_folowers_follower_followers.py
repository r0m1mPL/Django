# Generated by Django 4.0.3 on 2022-04-10 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_follower'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follower',
            old_name='folowers',
            new_name='followers',
        ),
    ]
