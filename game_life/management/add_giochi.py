from django.core.management.base import BaseCommand
from game_life.models import Gioco, CasaProduzione, Venditore
from datetime import date

class Command(BaseCommand):
    help = 'Aggiunge giochi demo con case di produzione e venditori'

    def handle(self, *args, **kwargs):
        # Crea o ottieni case di produzione
        casa1, _ = CasaProduzione.objects.get_or_create(nome="Ubisoft", defaults={"anno_fondazione": 1986, "sede": "Francia"})
        casa2, _ = CasaProduzione.objects.get_or_create(nome="Nintendo", defaults={"anno_fondazione": 1889, "sede": "Giappone"})

        # Crea o ottieni venditori
        vend1, _ = Venditore.objects.get_or_create(nome="Steam", defaults={"sito_web": "https://store.steampowered.com", "contatto_email": "support@steam.com"})
        vend2, _ = Venditore.objects.get_or_create(nome="Amazon", defaults={"sito_web": "https://www.amazon.it", "contatto_email": "support@amazon.it"})

        # Crea gioco
        gioco, created = Gioco.objects.get_or_create(
            titolo="Assassin's Creed",
            defaults={
                "descrizione": "Gioco d'azione e avventura nel passato.",
                "data_uscita": date(2007, 11, 13),
                "prezzo": 49.99,
                "genere": "Azione"
            }
        )

        # Aggiungi relazioni many-to-many
        gioco.case_produzione.set([casa1])
        gioco.venditori.set([vend1, vend2])

        if created:
            self.stdout.write(self.style.SUCCESS("Gioco 'Assassin's Creed' creato con successo."))
        else:
            self.stdout.write("Il gioco 'Assassin's Creed' esiste già.")
