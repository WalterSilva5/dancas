# Generated by Django 3.1.6 on 2021-05-18 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfit', '0013_playlist_desabilitada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='nome',
            field=models.CharField(default='', max_length=255, verbose_name='nome'),
        ),
    ]
