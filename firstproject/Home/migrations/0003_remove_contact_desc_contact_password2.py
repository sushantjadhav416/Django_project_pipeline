# Generated by Django 4.2.2 on 2023-07-05 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_remove_contact_date_contact_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='desc',
        ),
        migrations.AddField(
            model_name='contact',
            name='password2',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]