from django.urls import path
from .views import lista_productos

urlpatterns = [
    path('api/producto/', lista_productos),
]
