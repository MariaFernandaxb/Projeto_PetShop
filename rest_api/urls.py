from django.urls import path

from rest_api.views import  reserva, AgendamentoModelViewSet, inicio, ContatoAgendamentoModelViewSet

from rest_framework.routers import SimpleRouter


app_name = 'rest_api'

router = SimpleRouter()
router.register('agendamento', AgendamentoModelViewSet)
router.register('contato', ContatoAgendamentoModelViewSet)
# router.register('contato', ContatoModelViewSet)

urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    # path('hello_world/', hello_world, name='hello_world')
    path('reserva/', reserva, name='reserva')
]

urlpatterns += router.urls