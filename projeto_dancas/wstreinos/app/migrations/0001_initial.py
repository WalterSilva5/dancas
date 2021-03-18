# Generated by Django 3.1.5 on 2021-01-19 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aparelho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='nome')),
                ('dica', models.CharField(default='', max_length=255, null=True, verbose_name='dica')),
            ],
        ),
        migrations.CreateModel(
            name='Exercicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='nome')),
                ('dica', models.CharField(default='', max_length=255, null=True, verbose_name='dica')),
                ('series', models.IntegerField(default='', null=True, verbose_name='series')),
                ('duracao', models.CharField(default='', max_length=255, null=True, verbose_name='duracao')),
                ('carga', models.CharField(default='', max_length=255, null=True, verbose_name='carga')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=100, verbose_name='login')),
                ('senha', models.CharField(max_length=100, verbose_name='senha')),
            ],
        ),
    ]
