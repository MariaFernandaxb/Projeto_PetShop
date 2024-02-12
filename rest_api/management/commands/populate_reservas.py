
from django.core.management.base import BaseCommand

from reservadebanho.models import Reserva

from model_bakery import baker

class Command(BaseCommand):
    help = 'Criar reservas fakes de forma aleatória'

    def handle(self, *args, **options):
        total = 10

        self.stdout.write(
            self.style.WARNING(F'Gerando {total} reservas de banho')
        )

        for index in range(total):
            reserva = baker.make(Reserva)
            reserva.save()

            self.stdout.write(
                self.style.HTTP_INFO(F'Reserva {index + 1} criada')
            )

        self.stdout.write(
            self.style.SUCCESS('Todas as reservas foram criadas com sucesso')
        )

