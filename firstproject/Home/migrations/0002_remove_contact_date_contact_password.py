# Generated by Django 4.2.2 on 2023-06-29 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='date',
        ),
        migrations.AddField(
            model_name='contact',
            name='password',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
