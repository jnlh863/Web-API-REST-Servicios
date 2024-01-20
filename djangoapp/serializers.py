from rest_framework import serializers
from .models import Cliente, Pedidos

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'nombre', 'password', 'created_at')
        read_only_fields = ('created_at',)

   
class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedidos
        fields = ('id', 'id_client', 'descripcion', 'precio', 'created_at')
        read_only_fields = ('created_at',)