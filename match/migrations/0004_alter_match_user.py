# Generated by Django 4.1.7 on 2023-04-15 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('match', '0003_alter_match_location_alter_match_team1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.profile'),
        ),
    ]
