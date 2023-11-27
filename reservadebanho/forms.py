from django import forms
from reservadebanho.models import Reserva
from datetime import date

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nome_dono', 'nome_pet','telefone','observacoes','data_reserva','tamanho','turno']
        
        widgets = {
            'data_reserva': forms.DateInput(attrs={'type':'date'}),
        }
        
    def clean_data_reserva(self):
        data = self.cleaned_data['data_reserva']
        hoje = date.today()
        
        if data < hoje:
            raise forms.ValidationError('Não é permitido reservar nesta data.')
        
        qntdreserva = Reserva.objects.filter(data_reserva=data).count()

        if qntdreserva >= 4:
            raise forms.ValidationError('Já esgotou reservas para esse dia. Por favor, selecione outro.')
        
        
        return data