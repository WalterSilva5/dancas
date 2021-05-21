# Generated by Django 3.2.2 on 2021-05-21 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfit', '0014_auto_20210518_1034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=255, verbose_name='nome')),
                ('mensagem', models.CharField(default='', max_length=255, verbose_name='mensagem')),
                ('tipo', models.IntegerField(default=0, verbose_name='tipo')),
            ],
        ),
        migrations.DeleteModel(
            name='Aparelho',
        ),
        migrations.DeleteModel(
            name='Exercicio',
        ),
    ]