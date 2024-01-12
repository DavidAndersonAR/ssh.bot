from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from . models import AtivoEnel, TabelaArp, ShowBgpSu, ShowCdpNeiDet, ShowInStatus, ShowIntDes, ShowInterTran, ShowIpOsNei, ShowLog, ShowMacAddres, ShowRuning
from .forms import AtivoEnelModelForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
import paramiko
# Create your views here.

def visao_geral(request):
    return render(request, 'visao_geral.html')

def hosts(request):
    hosts = AtivoEnel.objects.all()
    
   
    if request.method == 'POST':
        new_form = AtivoEnelModelForm(request.POST)
        if new_form.is_valid():
            new_form.save()
            return redirect('hosts')
    else:
        new_form = AtivoEnelModelForm()
    return render(request, 'hosts.html', {'new_form':new_form, 'hosts':hosts})

def comparar_hosts(request):
    hosts = AtivoEnel.objects.all()
    
    return render(request, 'comparar_hosts.html', { 'hosts':hosts})

def comparar_hosts_lista(request, pk):
    host = get_object_or_404(AtivoEnel, pk=pk)
    
    return render(request, 'comparar_hosts_lista.html', { 'host':host})

def comparar_hosts_lista_arp(request, host_id):
    host = get_object_or_404(AtivoEnel, pk=host_id)
 
    # comando_arp = get_object_or_404(TabelaArp)

    saida_comando = TabelaArp.objects.filter(host_id=host_id)

    return render(request, 'comparar_hosts_lista_arp.html', {'saida_comando':saida_comando, 'host':host})


def result_hosts_lista_arp(request, pk):


    #saida_comando = TabelaArp.objects.filter(host_id=host_id)
    saida_comando = get_object_or_404(TabelaArp, pk=pk)

    return render(request, 'result_hosts_lista_arp.html', {'saida_comando':saida_comando})


def comparar_hosts_lista_arp_table_2(request, host_id):
    host = get_object_or_404(AtivoEnel, pk=host_id)
 
    # comando_arp = get_object_or_404(TabelaArp)

    saida_comando = TabelaArp.objects.filter(host_id=host_id)

    return render(request, 'comparar_hosts_lista_arp.html', {'saida_comando':saida_comando, 'host':host})
    



def comparar_hosts_lista_cdp(request, host_id):
    host = get_object_or_404(AtivoEnel, pk=host_id)

    saida_comando = ShowCdpNeiDet.objects.filter(host_id=host_id)
   
    return render(request, 'comparar_hosts_lista_arp.html', {'saida_comando':saida_comando, 'host':host})

def comparar_hosts_lista_inter_tran(request, host_id):
    host = get_object_or_404(AtivoEnel, pk=host_id)

    saida_comando = ShowInterTran.objects.filter(host_id=host_id)
 
    return render(request, 'comparar_hosts_lista_arp.html', {'saida_comando':saida_comando, 'host':host})

def comparar_hosts_lista_ip_os(request, host_id):
    host = get_object_or_404(AtivoEnel, pk=host_id)

    saida_comando = ShowIpOsNei.objects.filter(host_id=host_id)
   
    return render(request, 'comparar_hosts_lista_arp.html', {'saida_comando':saida_comando, 'host':host})

def comparar_hosts_lista_int_status(request, host_id):
    host = get_object_or_404(AtivoEnel, pk=host_id)
 
    saida_comando = ShowInStatus.objects.filter(host_id=host_id)
   

    return render(request, 'comparar_hosts_lista_arp.html', {'saida_comando':saida_comando, 'host':host})

def comparar_hosts_lista_inst_des(request, host_id):
    host = get_object_or_404(AtivoEnel, pk=host_id)
 
    # comando_arp = get_object_or_404(TabelaArp)

    saida_comando = ShowIntDes.objects.filter(host_id=host_id)
 
    return render(request, 'comparar_hosts_lista_arp.html', {'saida_comando':saida_comando, 'host':host})

def comparar_hosts_lista_bgp(request, host_id):
    host = get_object_or_404(AtivoEnel, pk=host_id)

    saida_comando = ShowBgpSu.objects.filter(host_id=host_id)
 
    return render(request, 'comparar_hosts_lista_arp.html', {'saida_comando':saida_comando, 'host':host})

def comparar_hosts_lista_run(request, host_id):
    host = get_object_or_404(AtivoEnel, pk=host_id)
 
 

    saida_comando = ShowRuning.objects.filter(host_id=host_id)

    return render(request, 'comparar_hosts_lista_arp.html', {'saida_comando':saida_comando, 'host':host})

def comparar_hosts_lista_log(request, host_id):
    host = get_object_or_404(AtivoEnel, pk=host_id)

    saida_comando = ShowLog.objects.filter(host_id=host_id)
  
    return render(request, 'comparar_hosts_lista_arp.html', {'saida_comando':saida_comando, 'host':host})

def comparar_hosts_lista_mac(request, host_id):
    host = get_object_or_404(AtivoEnel, pk=host_id)

    saida_comando = ShowMacAddres.objects.filter(host_id=host_id)
 
    return render(request, 'comparar_hosts_lista_arp.html', {'saida_comando':saida_comando, 'host':host})






def tabela_arp_view(request):
    arp_table = TabelaArp.objects.all()
    contexto = {'arp_table':arp_table}
    print(arp_table)

    return render(request, 'tabela_arp.html', contexto)



class HostOptionView(DetailView):
    model = AtivoEnel
    template_name = 'host_options_view.html'

def host_detail(request, pk):
    
    host = get_object_or_404(AtivoEnel, pk=pk)
    
   
    return render(request, 'host_detail.html', {'host': host})


#<<< comandos >>>

class HostOptionViewArp(DetailView):
    model = TabelaArp
    template_name = 'resultado_comando.html'
    context_object_name = 'tabela_arp'

    def get_object(self, queryset=None):
        # Recuperar o objeto TabelaArp com base na chave estrangeira host_id
        host_id = self.kwargs.get('pk')
        return self.model.objects.get(host_id=host_id)
    
def show_tabela_arp(request, host_id):
    
    host = get_object_or_404(AtivoEnel, pk=host_id)
 
    # comando_arp = get_object_or_404(TabelaArp)

    saida_comando = TabelaArp.objects.filter(host_id=host_id)
   
    print(host)
    print(saida_comando)
    

    return render(request, 'resultado_comando.html', {'saida_comando':saida_comando, 'hosts':host})


def show_comando(request, pk):
    saida_comando = get_object_or_404(TabelaArp, pk=pk)


    contexto = {
        'saida_comando_detail' : saida_comando,
     
    }

    return render(request,'resultado_comando.html', contexto)

def show_bgp_view(request, host_id):
    host = get_object_or_404(AtivoEnel, pk=host_id)
    saida_comando = ShowBgpSu.objects.filter(host_id=host_id)
    contexto = {
        'saida_comando' : saida_comando,
        'hosts':host
    }

    return render(request,'show_bgp.html', contexto)
def show_bgp(request, pk):
    saida_comando_detail_mac = get_object_or_404(ShowBgpSu, pk=pk)
    print(saida_comando_detail_mac)


    contexto = {
        'saida_comando_detail_mac' : saida_comando_detail_mac,
     
    }

    return render(request,'show_bgp.html',{'saida_comando_detail_mac' : saida_comando_detail_mac,} )

def show_mac_view(request, host_id):
    
    host = get_object_or_404(AtivoEnel, pk=host_id)
    saida_comando = ShowMacAddres.objects.filter(host_id=host_id)
    contexto = {
        'saida_comando' : saida_comando,
        'hosts':host
    }
    print(saida_comando)
    
    return render(request,'show_mac_view.html', contexto)
def show_mac(request, pk):
    saida_comando_detail_mac = get_object_or_404(ShowMacAddres, pk=pk)
    print(saida_comando_detail_mac)


    contexto = {
        'saida_comando_detail_mac' : saida_comando_detail_mac,
     
    }

    return render(request,'show_mac_view.html',{'saida_comando_detail_mac' : saida_comando_detail_mac,} )

def show_log_view(request, host_id):
    
    host = get_object_or_404(AtivoEnel, pk=host_id)
    saida_comando = ShowLog.objects.filter(host_id=host_id)
    contexto = {
        'saida_comando' : saida_comando,
        'hosts':host
    }

    return render(request,'show_log.html', contexto)
def show_log(request, pk):
    saida_comando_detail_mac = get_object_or_404(ShowLog, pk=pk)
    print(saida_comando_detail_mac)


    contexto = {
        'saida_comando_detail_mac' : saida_comando_detail_mac,
     
    }

    return render(request,'show_log.html',{'saida_comando_detail_mac' : saida_comando_detail_mac,} )

def show_ip_os_nei_view(request, host_id):
  
    host = get_object_or_404(AtivoEnel, pk=host_id)
    saida_comando = ShowIpOsNei.objects.filter(host_id=host_id)
    contexto = {
        'saida_comando' : saida_comando,
        'hosts':host
    }

    return render(request,'show_ip_os_nei.html', contexto)
def show_ip_os_nei(request, pk):
    saida_comando_detail_mac = get_object_or_404(ShowIpOsNei, pk=pk)
    print(saida_comando_detail_mac)


    contexto = {
        'saida_comando_detail_mac' : saida_comando_detail_mac,
     
    }

    return render(request,'show_ip_os_nei.html',{'saida_comando_detail_mac' : saida_comando_detail_mac,} )

def show_int_des_view(request, host_id):
  
    host = get_object_or_404(AtivoEnel, pk=host_id)
    saida_comando = ShowIntDes.objects.filter(host_id=host_id)
    contexto = {
        'saida_comando' : saida_comando,
        'hosts':host
    }

    return render(request,'show_int_des.html', contexto)
def show_int_des(request, pk):
    saida_comando_detail_mac = get_object_or_404(ShowIntDes, pk=pk)
    print(saida_comando_detail_mac)


    contexto = {
        'saida_comando_detail_mac' : saida_comando_detail_mac,
     
    }

    return render(request,'show_int_des.html',{'saida_comando_detail_mac' : saida_comando_detail_mac,} )

def show_int_tran_view(request, host_id):
  
    host = get_object_or_404(AtivoEnel, pk=host_id)
    saida_comando = ShowInterTran.objects.filter(host_id=host_id)
    contexto = {
        'saida_comando' : saida_comando,
        'hosts':host
    }

    return render(request,'show_int_tran.html', contexto)
def show_int_tran(request, pk):
    saida_comando_detail_mac = get_object_or_404(ShowInterTran, pk=pk)
    print(saida_comando_detail_mac)


    contexto = {
        'saida_comando_detail_mac' : saida_comando_detail_mac,
     
    }

    return render(request,'show_int_tran.html',{'saida_comando_detail_mac' : saida_comando_detail_mac,} )

def show_int_status_view(request, host_id):
   
    host = get_object_or_404(AtivoEnel, pk=host_id)
    saida_comando = ShowInStatus.objects.filter(host_id=host_id)
    contexto = {
        'saida_comando' : saida_comando,
        'hosts':host
    }

    return render(request,'show_int_status.html', contexto)
def show_int_status(request, pk):
    saida_comando_detail_mac = get_object_or_404(ShowInStatus, pk=pk)
    print(saida_comando_detail_mac)


    contexto = {
        'saida_comando_detail_mac' : saida_comando_detail_mac,
     
    }

    return render(request,'show_int_status.html',{'saida_comando_detail_mac' : saida_comando_detail_mac,} )


def show_cdp_view(request, host_id):
 
    host = get_object_or_404(AtivoEnel, pk=host_id)
    saida_comando = ShowCdpNeiDet.objects.filter(host_id=host_id)
    contexto = {
        'saida_comando' : saida_comando,
        'hosts':host
    }

    return render(request,'show_cdp.html', contexto)
def show_cdp(request, pk):
    saida_comando_detail_mac = get_object_or_404(ShowCdpNeiDet, pk=pk)
    print(saida_comando_detail_mac)


    contexto = {
        'saida_comando_detail_mac' : saida_comando_detail_mac,
     
    }

    return render(request,'show_cdp.html',{'saida_comando_detail_mac' : saida_comando_detail_mac,} )

def show_running_view(request, host_id):
    
    host = get_object_or_404(AtivoEnel, pk=host_id)
    saida_comando = ShowRuning.objects.filter(host_id=host_id)
    contexto = {
        'saida_comando' : saida_comando,
        'hosts':host
    }

    return render(request,'show_running.html', contexto)
def show_running(request, pk):
    saida_comando_detail_mac = get_object_or_404(ShowRuning, pk=pk)
    print(saida_comando_detail_mac)


    contexto = {
        'saida_comando_detail_mac' : saida_comando_detail_mac,
     
    }

    return render(request,'show_running.html',{'saida_comando_detail_mac' : saida_comando_detail_mac,} )

    
class HostOptionViewBgpSu(DetailView):
    model = ShowBgpSu
    template_name = 'host_options_view.html'
    context_object_name = 'tabela_bgp'

    def get_object(self, queryset=None):
        # Recuperar o objeto ShowBgpSu com base na chave estrangeira host_id
        host_id = self.kwargs.get('pk')
        return self.model.objects.get(host_id=host_id)
      
class HostOptionShowCdpNeiDet(DetailView):
    model = ShowCdpNeiDet
    template_name = 'host_options_view.html'
    context_object_name = 'tabela_cdpne'

    def get_object(self, queryset=None):
        # Recuperar o objeto ShowCdpNeiDet com base na chave estrangeira host_id
        host_id = self.kwargs.get('pk')
        return self.model.objects.get(host_id=host_id)
    
class HostOptionShowInStatus(DetailView):
    model = ShowInStatus
    template_name = 'host_options_view.html'
    context_object_name = 'tabela_intstatus'

    def get_object(self, queryset=None):
        # Recuperar o objeto ShowInStatus com base na chave estrangeira host_id
        host_id = self.kwargs.get('pk')
        return self.model.objects.get(host_id=host_id)
    
class HostOptionShowIntDes(DetailView):
    model = ShowIntDes
    template_name = 'host_options_view.html'
    context_object_name = 'tabela_intdes'

    def get_object(self, queryset=None):
        # Recuperar o objeto ShowIntDes com base na chave estrangeira host_id
        host_id = self.kwargs.get('pk')
        return self.model.objects.get(host_id=host_id)
    
class HostOptionShowInterTran(DetailView):
    model = ShowInterTran
    template_name = 'host_options_view.html'
    context_object_name = 'tabela_inttranc'

    def get_object(self, queryset=None):
        # Recuperar o objeto ShowInterTran com base na chave estrangeira host_id
        host_id = self.kwargs.get('pk')
        return self.model.objects.get(host_id=host_id)
    
class HostOptionShowIpOsNei(DetailView):
    model = ShowIpOsNei
    template_name = 'host_options_view.html'
    context_object_name = 'tabela_ipos'

    def get_object(self, queryset=None):
        # Recuperar o objeto ShowIpOsNei com base na chave estrangeira host_id
        host_id = self.kwargs.get('pk')
        return self.model.objects.get(host_id=host_id)
    
class HostOptionShowLog(DetailView):
    model = ShowLog
    template_name = 'host_options_view.html'
    context_object_name = 'tabela_log'

    def get_object(self, queryset=None):
        # Recuperar o objeto ShowLog com base na chave estrangeira host_id
        host_id = self.kwargs.get('pk')
        return self.model.objects.get(host_id=host_id)
    
class HostOptionShowMacAddres(DetailView):
    model = ShowMacAddres
    template_name = 'host_options_view.html'
    context_object_name = 'tabela_mac'

    def get_object(self, queryset=None):
        # Recuperar o objeto ShowMacAddres com base na chave estrangeira host_id
        host_id = self.kwargs.get('pk')
        return self.model.objects.get(host_id=host_id)
    
class HostOptionShowRuning(DetailView):
    model = ShowRuning
    template_name = 'host_options_view.html'
    context_object_name = 'tabela_run'

    def get_object(self, queryset=None):
        # Recuperar o objeto ShowRuning com base na chave estrangeira host_id
        host_id = self.kwargs.get('pk')
        return self.model.objects.get(host_id=host_id)

#<<< fim comandos >>>
class HostUpdateView(UpdateView):
    model = AtivoEnel
    form_class = AtivoEnelModelForm
    template_name = 'hosts_update.html'
    success_url = '/hosts/'

class HostDeleteView(DeleteView):
    model=AtivoEnel
    template_name = ''
    success_url = '/hosts/'
    pass
