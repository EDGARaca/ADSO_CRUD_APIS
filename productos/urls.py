from rest_framework.routers import DefaultRouter
from .views import ProductosViewSet

router = DefaultRouter() # Crea un enrutador por defecto 
router.register(r'productos', ProductosViewSet, basename='productos') # Registra el ViewSet con el prefijo 'productos'

urlpatterns = router.urls # Asigna las URLs generadas por el enrutador a urlpatterns

