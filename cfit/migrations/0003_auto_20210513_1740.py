# Generated by Django 3.1.6 on 2021-05-13 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfit', '0002_auto_20210513_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='login',
        ),
        migrations.AddField(
            model_name='usuario',
            name='usuario',
            field=models.CharField(default='teste', max_length=100, unique=True, verbose_name='usuario'),
            preserve_default=False,
        ),
    ]
