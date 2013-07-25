from django.db import models

class BancoDeDados(models.Model):
    banco = models.CharField(max_length=200)

class Ambiente(models.Model):
    ambiente = models.CharField(max_length=200)