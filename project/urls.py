
from django.contrib import admin
from django.urls import path

from catalogo.views import home, segunda, calculo


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('segunda_pagina', segunda),
    path('calculo', calculo)
]
