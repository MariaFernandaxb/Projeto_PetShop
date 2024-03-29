from django.urls import path

from rest_api.views import  *

from rest_framework.routers import SimpleRouter


app_name = 'rest_api'

router = SimpleRouter()
router.register('agendamento', AgendamentoModelViewSet)
router.register('contato', ContatoAgendamentoModelViewSet)
router.register('funcionario', FuncionarioModelViewSet)
# router.register('contato', ContatoModelViewSet)

urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    # path('hello_world/', hello_world, name='hello_world')
]

urlpatterns += router.urls