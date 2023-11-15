from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mensagem = models.TextField(blank=True, null=True)
    data = models.DateField(auto_now_add=True)

class Reserva(models.Model):  
    nome_pet = models.CharField(max_length=50)
    telefone = models.CharField(max_length=10)
    data_reserva = models.DateField()
    observacoes = models.TextField(blank=True, null=True)

