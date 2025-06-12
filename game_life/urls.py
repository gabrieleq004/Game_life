from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('recensione/<int:gioco_id>/', views.inserisci_recensione, name='inserisci_recensione'),  # ⬅️ nuova rotta
]
