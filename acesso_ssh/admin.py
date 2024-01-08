from django.contrib import admin
from .models import TabelaArp

# Register your models here.
@admin.register
class TabelaArpAdmin(admin.ModelAdmin):
    list_display = ('arp')
    list_filter = ('id')

admin.site.register(TabelaArp)