from django.contrib import admin
from reservadebanho.models import Reserva

# Register your models here.
@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['nome_dono', 'nome_pet','data_reserva','tamanho','turno']
    search_fields = ['nome_dono','nome_pet']
    list_filter = ['data_reserva','tamanho', 'turno']