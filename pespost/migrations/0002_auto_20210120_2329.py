# Generated by Django 3.1.5 on 2021-01-20 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pespost', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='player_style',
            field=models.CharField(max_length=20, verbose_name='選手タイプ'),
        ),
    ]
