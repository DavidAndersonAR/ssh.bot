"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from acesso_ssh.views import visao_geral, hosts, tabela_arp_view, HostOptionView, HostOptionViewArp, HostUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', visao_geral, name='visao_geral'),
    path('hosts/', hosts, name='hosts'),
    path('tabela_arp_view/', tabela_arp_view, name='tabela_arp_view'),
    #path('host_options_view/<int:pk>/', host_options_view, name='host_options_view'),
    path('host_options_view/<int:pk>/', HostOptionView.as_view(), name='host_options_view'),
    path('host_options_view/arp/<int:pk>/', HostOptionViewArp.as_view(), name='show_arp_view'),
    path('update_view/<int:pk>/', HostUpdateView.as_view(), name='update_view'),
    
]
