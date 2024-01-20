from django.urls import path
from .api import all, login, register, client_details, all_services, add_services, services_client, service_details

urlpatterns =[
    #CLIENTE
    path('user/all', all, name = 'all'),
    path('user/add', register, name ='register'),
    path('user/login', login, name ='login'),
    path('user/<int:pk>', client_details, name='client_details'),

    #SERVICIOS
    path('user/services', all_services, name = 'all_services'),
    path('user/add_services', add_services, name = 'add_services'),
    path('user/progress/<int:idClient>', services_client, name= 'services_client'),
    path('user/details/<int:idPedido>', service_details, name = 'service_details')
]
























#from rest_framework import routers
#from .api import LoginViewSet

#router = routers.DefaultRouter()

#router.register('api/login', LoginViewSet, 'login')



#urlpatterns = router.urls