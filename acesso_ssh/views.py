from django.shortcuts import redirect, render
from . models import AtivoEnel, TabelaArp
from .forms import AtivoEnelModelForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, View

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


def tabela_arp_view(request):
    arp_table = TabelaArp.objects.all()
    contexto = {'arp_table':arp_table}
    print(arp_table)

    return render(request, 'tabela_arp.html', contexto)

# def host_options_view(request, pk):
#     teste=pk
#     arp_table = TabelaArp.objects.filter(host_id__host__icontains=teste)


#     return render(request, 'host_options_view.html')

class HostOptionView(DetailView):
    model = AtivoEnel.objects.all()[:100]
    template_name = 'host_options_view.html'




class HostOptionViewArp(DetailView):
    model = TabelaArp
    template_name = 'host_options_view.html'
    context_object_name = 'tabela_arp'

    def get_object(self, queryset=None):
        # Recuperar o objeto TabelaArp com base na chave estrangeira host_id
        host_id = self.kwargs.get('pk')
        return self.model.objects.get(host_id=host_id)

class HostUpdateView(UpdateView):
    model = AtivoEnel
    form_class = AtivoEnelModelForm
    template_name = 'hosts_update.html'
    success_url = '/hosts/'


