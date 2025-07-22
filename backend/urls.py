from django.urls import path, include
from django.contrib import admin
from users import views  # importa views aquí


urlpatterns = [
    path('api/', include('movies.urls')), # Esto activa todas las rutas de la app movies
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('', views.test, name='root_test'),  # <-- esta línea agrega la ruta raíz
]
