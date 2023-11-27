from django.db import models

# Create your models here.
class Reserva(models.Model):  
    TAMANHO_OPCOES = (
        (0, 'Pequeno'),
        (1, 'Medio'),
        (2, 'Grande')
    )
    TURNO_OPCOES = (
        ('manha','Manhã'),
        ('tarde', 'Tarde')
    )
    nome_dono = models.CharField(verbose_name='Nome do Dono', max_length=50)
    nome_pet = models.CharField(verbose_name='Nome do Pet', max_length=50)
    telefone = models.CharField(verbose_name='Telefone',max_length=10)
    data_reserva = models.DateField(verbose_name='Data da Reserva')
    observacoes = models.TextField(verbose_name='Observações', blank=True, null=True)
    tamanho = models.IntegerField(verbose_name='Tamanho',choices=TAMANHO_OPCOES)
    turno = models.CharField(verbose_name='Turno', max_length=10, choices=TURNO_OPCOES)
    
    class Meta:
        verbose_name = 'Reserva de Banho'
        verbose_name_plural = 'Reservas de Banhos'
        