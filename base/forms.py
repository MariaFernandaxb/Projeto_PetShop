from django import forms 

from base.models import Contato, Reserva
class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato

        fields = ['nome', 'email', 'mensagem']

        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'placeholder': 'Insira seu nome aqui'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Insira seu e-mail aqui'
                }
            ),
            'mensagem': forms.Textarea(
                attrs={
                    'placeholder': 'Insira sua mensagem aqui'
                }
            ),
        }

        labels = {
            'nome': 'Nome:',
            'email': 'E-mail:',
            'mensagem': 'Mensagem:'
        }

class DateInput(forms.DateInput):
    input_type = 'date'
class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva

        fields = ['nome_pet', 'telefone', 'data_reserva', 'observacoes']

        widgets = {
            'nome_pet': forms.TextInput(
                attrs={
                    'placeholder': 'Insira o nome do pet aqui'
                }
            ),
            'telefone': forms.TextInput(
                attrs={
                    'placeholder': 'Insira o telefone aqui'
                }
            ),
            'data_reserva': DateInput(),
            'observacoes': forms.Textarea(
                attrs={
                    'placeholder': 'Insira as observações aqui'
                }
            )
        }

        labels = {
            'nome_pet': 'Nome do pet:',
            'telefone': 'Telefone:',
            'data_reserva': 'Data da reserva:',
            'observacoes': 'Observações:'
        }
