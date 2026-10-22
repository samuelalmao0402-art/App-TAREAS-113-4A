from django.urls import path
from .import views

urlpatterns = [
   
    path('', views.login_pagina, name= 'login_pagina'),
    path('tareas/', views.inicio, name='inicio'),
    path('crear/', views.crear_tarea, name='crear_tarea'),
    path('detalle/<int:id>', views.detalle_tarea, name='detalle_tarea'),
    path('editar/<int:id>', views.editar_tarea, name='editar_tarea'),
    path('eliminar/<int:id>', views.eliminar_tarea, name='eliminar_tarea'),

    #API REST PARA AUTENTICACION
    path('api/login/', views.LoginAPIView.as_view(), name='login_api'),

    # API RESET para listar tarea

    path('api/tareas/', views.TareasApiView.as_view(), name='api_tareas')
]

