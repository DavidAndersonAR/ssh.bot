from django.db import models

# Create your models here.

class Empresa(models.Model):
    id = models.IntegerField(primary_key=True)
    empresa = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.empresa
    
class Localidade(models.Model):
    id = models.IntegerField(primary_key=True)
    empresa = models.ForeignKey(Empresa,on_delete=models.SET_NULL ,blank=True, null=True)
    localidade = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.localidade

class AtivoEnel(models.Model):
    id = models.IntegerField(primary_key=True)
    host = models.CharField(max_length=200, blank=True, null=True)
    ip = models.CharField(max_length=200, blank=True, null=True)
    localidade = models.ForeignKey(Localidade, on_delete=models.SET_NULL ,blank=True, null=True)
    empresa = models.ForeignKey(Empresa,on_delete=models.SET_NULL ,blank=True, null=True)
    modelo = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.host


class TabelaArp(models.Model):
    id = models.IntegerField(primary_key=True)
    host = models.ForeignKey(AtivoEnel, on_delete=models.SET_NULL,blank=True, null=True)
    arp = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.host} - arp'

   
        
    