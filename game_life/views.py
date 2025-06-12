from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Gioco, Recensione, Cliente  # importa i modelli
from .forms import RecensioneForm


def home(request):
    return render(request, 'game_life/home.html')


@login_required
def catalogo(request):
    giochi = Gioco.objects.all()
    form = RecensioneForm()
    return render(request, 'game_life/catalogo.html', {'giochi': giochi, 'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('catalogo')
        else:
            print("Form non valido:", form.errors.as_ul())
            print("Dati POST:", request.POST)
    else:
        form = AuthenticationForm()
    return render(request, 'game_life/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('catalogo')
    else:
        form = UserCreationForm()
    return render(request, 'game_life/register.html', {'form': form})


@login_required
def inserisci_recensione(request, gioco_id):
    gioco = get_object_or_404(Gioco, id=gioco_id)

    if request.method == 'POST':
        form = RecensioneForm(request.POST)
        if form.is_valid():
            recensione = form.save(commit=False)
            nome_cliente = form.cleaned_data['nome_cliente']
            cliente, created = Cliente.objects.get_or_create(nome=nome_cliente)
            recensione.cliente = cliente
            recensione.gioco = gioco
            recensione.save()
            return redirect('catalogo')
    return redirect('catalogo')
