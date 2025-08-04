
from django.urls import path, include   

urlpatterns = [
    path('api/', include('productos.urls')), # Incluye las URLs del app 'productos' bajo el prefijo 'api'
]
