from django.contrib import admin
from django.urls import path, include
from django.urls import reverse_lazy

LOGIN_URL = reverse_lazy('login')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('game_life.urls')),
]
