# Generated by Django 5.2.1 on 2025-05-22 10:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CasaProduzione',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Venditore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Gioco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=100)),
                ('case_produzione', models.ManyToManyField(related_name='giochi_prodotti', to='game_life.casaproduzione')),
                ('venditori', models.ManyToManyField(related_name='giochi_venduti', to='game_life.venditore')),
            ],
        ),
        migrations.CreateModel(
            name='Acquisto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acquisti', to='game_life.cliente')),
                ('gioco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acquisti', to='game_life.gioco')),
            ],
        ),
        migrations.CreateModel(
            name='Recensione',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenuto', models.TextField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recensioni', to='game_life.cliente')),
                ('gioco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recensioni', to='game_life.gioco')),
            ],
        ),
    ]
