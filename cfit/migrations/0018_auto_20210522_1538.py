# Generated by Django 3.1.6 on 2021-05-22 18:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfit', '0017_auto_20210522_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagamento',
            name='data',
            field=models.DateField(default=datetime.datetime(2021, 5, 22, 15, 38, 41, 594013), verbose_name='data'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.CharField(default='email', max_length=250, verbose_name='email'),
        ),
    ]
