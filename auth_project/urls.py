from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),  # Inclui as URLs da sua aplicação de usuários
    # Outras URLs do seu projeto, se houver
]