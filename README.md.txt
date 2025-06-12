
# Game Life – Sistema Informativo per la Vendita e Recensione di Videogiochi

## 1. Analisi e Progettazione Concettuale

Il sistema informativo "Game Life" gestisce informazioni relative a:
- **Clienti**: utenti registrati con dati personali.
- **Giochi**: titoli videoludici con informazioni come descrizione, prezzo, genere, data di uscita.
- **Case di produzione**: aziende produttrici dei giochi.
- **Venditori**: piattaforme o aziende che distribuiscono i giochi.
- **Recensioni**: valutazioni e commenti degli utenti sui giochi acquistati.
- **Acquisti**: relazioni tra clienti e giochi acquistati.

### Entità principali:
- **Cliente** (id, nome, email, data_registrazione)
- **Gioco** (id, titolo, descrizione, data_uscita, prezzo, genere)
- **CasaProduzione** (id, nome, anno_fondazione, sede)
- **Venditore** (id, nome, sito_web, contatto_email)
- **Recensione** (id, contenuto, voto, data_pubblicazione)
- **Acquisto** (id, cliente_id, gioco_id, data, metodo_pagamento)

### Relazioni:
- Un **gioco** può avere più **case di produzione** e viceversa (N:M)
- Un **gioco** può essere venduto da più **venditori** e viceversa (N:M)
- Un **cliente** può acquistare più **giochi**, e ogni acquisto è tracciato con data e metodo di pagamento.
- Un **cliente** può recensire un gioco una sola volta.

## 2. Progettazione Logica

Il modello logico derivato è basato su Django ORM:
- ForeignKey per le relazioni 1:N
- ManyToManyField per le relazioni N:M
- Uso di `related_name` per una navigazione semantica tra modelli

Esempi di vincoli:
- `unique=True` su email e titoli
- `default` su date e metodi di pagamento
- `choices` per i metodi di pagamento per assicurare consistenza nei dati

## 3. Implementazione in Django

Tecnologie usate:
- **Django** per backend e ORM
- **Template engine Django** per rendering HTML
- **Bootstrap** per la grafica responsiva
- **SQLite** come database di sviluppo

### Funzionalità implementate:
- Visualizzazione catalogo giochi (con pagina dettagli)
- Registrazione e autenticazione clienti
- Inserimento e consultazione recensioni
- Acquisto giochi con metodo di pagamento
- Storico acquisti per cliente

## Avvio del progetto

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Struttura del progetto

- `models.py` – definizione delle entità
- `views.py` – gestione delle logiche di business
- `templates/` – interfaccia utente
- `static/` – risorse grafiche (CSS/JS)

Autore: Gabriele quintiliani
Università di napoli parthenope
