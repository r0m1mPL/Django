# Generated by Django 4.0.2 on 2022-04-09 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='answers',
            field=models.ManyToManyField(blank=True, to='quiz_app.Answer', verbose_name='Answers'),
        ),
    ]
