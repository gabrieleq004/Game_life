from django.db import models
from datetime import date

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True, default='cliente@example.com')  # Evita errore iniziale
    data_registrazione = models.DateField(default=date.today)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']


class CasaProduzione(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    anno_fondazione = models.IntegerField(default=2000)
    sede = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']


class Venditore(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    sito_web = models.URLField(blank=True, null=True)
    contatto_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']


class Gioco(models.Model):
    titolo = models.CharField(max_length=100, unique=True)
    descrizione = models.TextField(blank=True, null=True)
    data_uscita = models.DateField(default=date.today)
    prezzo = models.DecimalField(max_digits=6, decimal_places=2, default=59.99)
    genere = models.CharField(max_length=50, default='Azione', help_text="Es: Azione, Avventura, Puzzle")
    case_produzione = models.ManyToManyField(CasaProduzione, related_name='giochi_prodotti')
    venditori = models.ManyToManyField(Venditore, related_name='giochi_venduti')

    def __str__(self):
        return self.titolo

    class Meta:
        ordering = ['-data_uscita']


class Recensione(models.Model):
    contenuto = models.TextField()
    voto = models.PositiveSmallIntegerField(default=5)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='recensioni')
    gioco = models.ForeignKey(Gioco, on_delete=models.CASCADE, related_name='recensioni')
    data_pubblicazione = models.DateField(default=date.today)

    def __str__(self):
        return f"Recensione di {self.cliente} su {self.gioco}"

    class Meta:
        ordering = ['-data_pubblicazione']


class Acquisto(models.Model):
    METODI_PAGAMENTO = [
        ('Carta', 'Carta di credito'),
        ('PayPal', 'PayPal'),
        ('Bonifico', 'Bonifico bancario'),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='acquisti')
    gioco = models.ForeignKey(Gioco, on_delete=models.CASCADE, related_name='acquisti')
    data = models.DateField(default=date.today)
    metodo_pagamento = models.CharField(
        max_length=20,
        choices=METODI_PAGAMENTO,
        default='Carta',
        help_text="Metodo utilizzato per il pagamento"
    )

    def __str__(self):
        return f"{self.cliente} ha comprato {self.gioco} il {self.data}"

    class Meta:
        ordering = ['-data']
