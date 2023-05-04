# Generated by Django 4.1.7 on 2023-04-15 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0004_alter_match_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='comments',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='team1_result',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='team2_result',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]