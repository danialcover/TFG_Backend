# Generated by Django 4.1.7 on 2023-04-10 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='league',
            old_name='any',
            new_name='year',
        ),
    ]