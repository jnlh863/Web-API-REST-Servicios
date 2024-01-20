# from rest_framework import viewsets, permissions
# from rest_framework.views import APIView
from djangoapp.models import Cliente, Pedidos
from rest_framework.response import Response
from .serializers import ClienteSerializer, PedidoSerializer
from rest_framework.decorators import api_view
from rest_framework import status


#CLIENTE
@api_view(['GET'])
def all(request):
    #Registros
    if request.method == 'GET':
        users = Cliente.objects.all()
        users_serializer = ClienteSerializer(users,many=True)
        return Response(users_serializer.data, status= status.HTTP_200_OK)


@api_view(['POST'])
def login(request):
    #Login
    if request.method == 'POST':
        user_serializer= ClienteSerializer(data = request.data)

        if user_serializer.is_valid() == False:
            name_client = Cliente.objects.filter(nombre = request.data.get('nombre')).first()
            client_serializer = ClienteSerializer(name_client)
            
            if client_serializer.data.get('password') == request.data.get('password'):
                return Response(client_serializer.data, status = status.HTTP_200_OK)
            return Response({'message':'Los datos son incorrectos, intentelo de nuevo'}, status= status.HTTP_409_CONFLICT)
        return Response({'message': 'Este usuario no existe, registrese'}, status = status.HTTP_400_BAD_REQUEST)
        

@api_view(['POST'])
def register(request):
    #Registro
    if request.method == 'POST':

       #Validar que los datos no sean repetidos
        name_client = Cliente.objects.filter(nombre = request.data.get('nombre')).first()
        client_serializer = ClienteSerializer(name_client)

        pass_client = Cliente.objects.filter(password = request.data.get('password')).first()
        pass_serializer = ClienteSerializer(pass_client)
            
        if client_serializer.data.get('password') == request.data.get('password'):
             return Response({'message': 'Este usuario ya existe, inicie sesión'}, status = status.HTTP_409_CONFLICT)
       
        if client_serializer.data.get('nombre') == request.data.get('nombre'):
             return Response({'message': 'Este nombre de usuario ya esta en uso'}, status = status.HTTP_409_CONFLICT)
       
        if pass_serializer.data.get('password') == request.data.get('password'):
             return Response({'message': 'Las contraseñas no se pueden repetir'}, status = status.HTTP_409_CONFLICT)


        #Registro
        user_serializer= ClienteSerializer(data = request.data)
        caracteres = ['#','$','%','&', '@']
        if user_serializer.is_valid():
            user_validated = user_serializer.validated_data
            if any(caracter in user_validated.get('nombre') for caracter in caracteres):
                if any(caracter in user_validated.get('password') for caracter in caracteres):
                    user_serializer.save()
                    return Response(user_serializer.data, status = status.HTTP_201_CREATED)
                return Response({'message': 'La contraseña debe contener al menos uno de estos caracteres @, #, $, %, &'},
                                        status = status.HTTP_406_NOT_ACCEPTABLE)
            return Response({'message': 'El nombre debe contener al menos uno de estos caracteres @, #, $, %, &'},
                                    status = status.HTTP_406_NOT_ACCEPTABLE)
        return Response({'message':'Nombre (Max, 60), Contraseña (Max, 10)'}, status= status.HTTP_400_BAD_REQUEST)



@api_view(['PUT','DELETE'])
def client_details(request,pk = None):

    client = Cliente.objects.filter(id = pk).first()

    if client:  
        #Actualizar cuenta
        if request.method == 'PUT':
            caracteres = ['@','#','$','%','&']
            client_serializer = ClienteSerializer(client, data = request.data)

            if client_serializer.is_valid():
                client_validated = client_serializer.validated_data
                if any(caracter in client_validated.get('nombre') for caracter in caracteres):
                    if any(caracter in client_validated.get('password') for caracter in caracteres):
                        client_serializer.save()
                        return Response({'message': 'Información actualizada'}, status = status.HTTP_200_OK)
                    return Response({'message': 'La contraseña debe contener al menos uno de estos caracteres @, #, $, %, &'},
                                            status = status.HTTP_406_NOT_ACCEPTABLE)
                return Response({'message': 'El nombre debe contener al menos uno de estos caracteres @, #, $, %, &'},
                                        status = status.HTTP_406_NOT_ACCEPTABLE)
             
            return Response({'message': 'Error, verifique el nombre y contraseña'}, status = status.HTTP_400_BAD_REQUEST)

        #Eliminar cuenta
        elif request.method == 'DELETE':
            client.delete()
            return Response({'message': 'Cuenta eliminada'}, status=status.HTTP_200_OK)
        
    return Response({'message': 'Este usuario no existe, registrese'}, status = status.HTTP_400_BAD_REQUEST)


#PEDIDOS
@api_view(['GET'])
def all_services(request):
    #Registro
    if request.method == 'GET':
        pedidos = Pedidos.objects.all()
        pedidos_serializer = PedidoSerializer(pedidos,many=True)
        return Response(pedidos_serializer.data, status= status.HTTP_200_OK)


@api_view(['POST'])
def add_services(request):
    #Registro 
    if request.method == 'POST':
        pedidos_serializer= PedidoSerializer(data = request.data)
        if pedidos_serializer.is_valid():
            pedidos_serializer.save()
            return Response({'message': 'Servicio registrado'}, status = status.HTTP_201_CREATED)
        return Response({'message':'Hubo un error, intentelo de nuevo'}, status= status.HTTP_400_BAD_REQUEST)

        
@api_view(['GET'])
def services_client(request, idClient = None):

    service_client = Pedidos.objects.filter(id_client = idClient)

    if service_client:
        if request.method == 'GET':
            service_serializer = PedidoSerializer(service_client,many=True)
            return Response(service_serializer.data, status = status.HTTP_200_OK)
        
    return Response({'message': 'Hubo un error, intentelo de nuevo'}, status = status.HTTP_400_BAD_REQUEST)


@api_view(['PUT','DELETE'])
def service_details(request, idPedido = None):

    service = Pedidos.objects.filter(id = idPedido).first()

    if service:    
        #Actualizar servicio
        if request.method == 'PUT':
            service_serializer = PedidoSerializer(service,data = request.data)
            if service_serializer.is_valid():
                service_serializer.save()
                return Response({'message':'Información actualizada'},status = status.HTTP_200_OK)
            return Response(service_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        #Eliminar servicio
        elif request.method == 'DELETE':
            service.delete()
            return Response({'message': 'Pedido cancelado'}, status=status.HTTP_200_OK)
        
    return Response({'message': 'Hubo un error, intentelo de nuevo'}, status = status.HTTP_400_BAD_REQUEST)