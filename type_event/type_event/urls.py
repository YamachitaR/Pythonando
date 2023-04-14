"""
URL configuration for type_event project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    # Esse include me parece que e o mesmo que foi adicionado la em cima do pacote
    #depois vamos criar um arquivo chamado urls,py dentro do usuarios
    path('usuarios/', include('usuarios.urls')),

    path('eventos/', include('eventos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# + static estamos usando para trabalhar como nossa imagem que usuario upa
# settings.MEDIA_URL esta acessando o valor da variavel MEDIA_URL, nesse caso o valor é media
# resumindo, estamos consertando a roda, pois no banco de dados esta salvo so como logo/imagem.png
# mas queremos que esteja /media/logo/imagem.png

 