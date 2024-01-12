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
from acesso_ssh.views import visao_geral, hosts, tabela_arp_view, HostOptionView, HostOptionViewArp, HostUpdateView, show_log_view, show_mac_view, show_bgp_view, show_mac
from acesso_ssh.views import show_tabela_arp, host_detail, show_comando, show_running_view, show_cdp_view, show_int_status_view, show_int_tran_view, show_int_des_view, show_ip_os_nei_view
from acesso_ssh.views import show_bgp,show_log,show_ip_os_nei,show_int_des,show_int_tran,show_int_status,show_cdp,show_running, comparar_hosts, comparar_hosts_lista,comparar_hosts_lista_arp
from acesso_ssh.views import comparar_hosts_lista_cdp, comparar_hosts_lista_inter_tran,comparar_hosts_lista_ip_os,comparar_hosts_lista_int_status,comparar_hosts_lista_inst_des,comparar_hosts_lista_bgp,comparar_hosts_lista_run,comparar_hosts_lista_log,comparar_hosts_lista_mac
from acesso_ssh.views import result_hosts_lista_arp, comparar_hosts_lista_arp_table_2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', visao_geral, name='visao_geral'),
    path('hosts/', hosts, name='hosts'),
    path('comparar_hosts/', comparar_hosts, name='comparar_hosts'),
    path('comparar_hosts_list/<int:pk>/', comparar_hosts_lista, name='comparar_hosts_lista'),

    path('comparar_hosts_list/arp/<int:host_id>/', comparar_hosts_lista_arp, name='comparar_hosts_lista_arp'),
    path('result_hosts_list/arp/<int:pk>/', result_hosts_lista_arp, name='result_hosts_lista_arp'),
    path('comparar_hosts_lista_arp_table_2/<int:host_id>/', comparar_hosts_lista_arp_table_2, name='comparar_hosts_lista_arp_table_2'),

    path('comparar_hosts_list/cdp/<int:host_id>/', comparar_hosts_lista_cdp, name='comparar_hosts_lista_cdp'),
    path('comparar_hosts_list/int_tranc/<int:host_id>/', comparar_hosts_lista_inter_tran, name='comparar_hosts_lista_inter_tran'),
    path('comparar_hosts_list/ip_os/<int:host_id>/', comparar_hosts_lista_ip_os, name='comparar_hosts_lista_ip_os'),
    path('comparar_hosts_list/int_status/<int:host_id>/', comparar_hosts_lista_int_status, name='comparar_hosts_lista_int_status'),
    path('comparar_hosts_list/int_des/<int:host_id>/', comparar_hosts_lista_inst_des, name='comparar_hosts_lista_inst_des'),
    path('comparar_hosts_list/bgp/<int:host_id>/', comparar_hosts_lista_bgp, name='comparar_hosts_lista_bgp'),
    path('comparar_hosts_list/run/<int:host_id>/', comparar_hosts_lista_run, name='comparar_hosts_lista_run'),
    path('comparar_hosts_list/log/<int:host_id>/', comparar_hosts_lista_log, name='comparar_hosts_lista_log'),
    path('comparar_hosts_list/mac/<int:host_id>/', comparar_hosts_lista_mac, name='comparar_hosts_lista_mac'),

    path('tabela_arp_view/', tabela_arp_view, name='tabela_arp_view'),
    #path('host_options_view/<int:pk>/', host_options_view, name='host_options_view'),
    path('host_options_view/<int:pk>/', HostOptionView.as_view(), name='host_options_view'),
    path('host_options_view/arp/<int:pk>/', HostOptionViewArp.as_view(), name='show_arp_view'),

    # path('show_tabela_arp/arp/<int:pk>/', show_tabela_arp, name='show_tabela_arp'),
    path('show_tabela_arp/<int:host_id>/', show_tabela_arp, name='show_tabela_arp'),
    path('show_comando/<int:pk>/', show_comando, name='show_comando'),
    path('host_detail/<int:pk>/', host_detail, name='host_detail'),
    path('update_view/<int:pk>/', HostUpdateView.as_view(), name='update_view'),

    #urls do running
    path('show_comando/show_running/<int:host_id>/', show_running_view, name='show_running_view'),
    path('show_comando_running/<int:pk>/', show_running, name='show_running'),
    #>>>>>>>>>>>>>>>

    #urls do cdp
    path('show_cdp/<int:host_id>/', show_cdp_view, name='show_cdp_view'),
    path('show_comando_cdp/<int:pk>/', show_cdp, name='show_cdp'),
    #>>>>>>>>>>>>>>>

    #urls do int status
    path('show_comando/show_int_status_view/<int:host_id>/', show_int_status_view, name='show_int_status_view'),
    path('show_comando_int_status_view/<int:pk>/', show_int_status, name='show_int_status'),
    #>>>>>>>>>>>>>>>

    #urls do int tran
    path('show_comando/show_int_tran_view/<int:host_id>/', show_int_tran_view, name='show_int_tran_view'),
    path('show_comando_int_tran_view/<int:pk>/', show_int_tran, name='show_int_tran'),
    #>>>>>>>>>>>>>>>

    #urls do int des
    path('show_comando/show_int_des_view/<int:host_id>/', show_int_des_view, name='show_int_des_view'),
    path('show_comando_int_des_view/<int:pk>/', show_int_des, name='show_int_des'),
    #>>>>>>>>>>>>>>>

    #urls do ip os ne
    path('show_comando/show_ip_os_nei_view/<int:host_id>/', show_ip_os_nei_view, name='show_ip_os_nei_view'),
    path('show_comando_ip_os_nei_view/<int:pk>/', show_ip_os_nei, name='show_ip_os_nei'),
    #>>>>>>>>>>>>>>>>

    #urls do log
    path('show_comando/show_log_view/<int:host_id>/', show_log_view, name='show_log_view'),
    path('show_comando_log_view/<int:pk>/', show_log, name='show_log'),
    #>>>>>>>>>>

    #urls do mac
    path('show_comando/show_mac_view/<int:host_id>/', show_mac_view, name='show_mac_view'),
    path('show_comando_mac_view/<int:pk>/', show_mac, name='show_mac'),
    #>>>>>>>>>>>

    #urls do bgp
    path('show_comando/show_bgp_view/<int:host_id>/', show_bgp_view, name='show_bgp_view'),
    path('show_comando_bgp_view/<int:host_id>/', show_bgp, name='show_bgp'),
    #>>>>>>>>>>>
    
]
