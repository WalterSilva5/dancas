from django.db import models


class Usuario(models.Model):
    login = models.CharField('login', max_length=100, null=False, blank=False, unique=True)
    senha = models.CharField('senha', max_length=100, null=False, blank=False)
    bloqueado = models.BooleanField('bloqueado', default=False)
    professor = models.BooleanField('professor', default=False)

class Aparelho(models.Model):
    nome = models.CharField('nome', max_length=255, unique=True)
    dica = models.CharField('dica', max_length=255, null=True, default='')


class Exercicio(models.Model):
    nome = models.CharField('nome', max_length=255, unique=True)
    dica = models.CharField('dica', max_length=255, null=True, default='')
    series = models.IntegerField('series', null=True, default='')
    duracao = models.CharField('duracao', max_length=255, null=True, default='')
    carga = models.CharField('carga', null=True, default='', max_length=255)