from django.urls import path
from reservadebanho.views import criar_reserva

app_name ='reserva'

urlpatterns = [
    path('criar/', criar_reserva, name='criar_reserva')
]