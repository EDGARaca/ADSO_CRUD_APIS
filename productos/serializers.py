from rest_framework import serializers
from .models import Productos

class ProductosSerializer(serializers.ModelSerializer):
    fecha_creacion = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)
    fecha_ultima_modificacion = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)

    class Meta:
        model = Productos
        fields = '__all__'  # Serializa todos los campos del modelo Productos
        