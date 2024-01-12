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
    comando = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.host} - arp'
    
class ShowCdpNeiDet(models.Model):
    id = models.IntegerField(primary_key=True)
    host = models.ForeignKey(AtivoEnel, on_delete=models.SET_NULL,blank=True, null=True)
    comando = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.host} - NEIDET'
    
class ShowInterTran(models.Model):
    id = models.IntegerField(primary_key=True)
    host = models.ForeignKey(AtivoEnel, on_delete=models.SET_NULL,blank=True, null=True)
    comando = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.host} - Interface tranc'

   
class ShowIpOsNei(models.Model):
    id = models.IntegerField(primary_key=True)
    host = models.ForeignKey(AtivoEnel, on_delete=models.SET_NULL,blank=True, null=True)
    comando = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.host} - Show ip os nei'

   
class ShowInStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    host = models.ForeignKey(AtivoEnel, on_delete=models.SET_NULL,blank=True, null=True)
    comando = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.host} - ShowInStatus'
    
class ShowMacAddres(models.Model):
    id = models.IntegerField(primary_key=True)
    host = models.ForeignKey(AtivoEnel, on_delete=models.SET_NULL,blank=True, null=True)
    comando = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.host} - ShowMacAddres'
    
class ShowIntDes(models.Model):
    id = models.IntegerField(primary_key=True)
    host = models.ForeignKey(AtivoEnel, on_delete=models.SET_NULL,blank=True, null=True)
    comando = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.host} - ShowIntDes'

   
class ShowBgpSu(models.Model):
    id = models.IntegerField(primary_key=True)
    host = models.ForeignKey(AtivoEnel, on_delete=models.SET_NULL,blank=True, null=True)
    comando = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.host} - ShowBgpSu'

   
class ShowRuning(models.Model):
    id = models.IntegerField(primary_key=True)
    host = models.ForeignKey(AtivoEnel, on_delete=models.SET_NULL,blank=True, null=True)
    comando = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.host} - ShowRuning'

   
class ShowLog(models.Model):
    id = models.IntegerField(primary_key=True)
    host = models.ForeignKey(AtivoEnel, on_delete=models.SET_NULL,blank=True, null=True)
    comando = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.host} - ShowLog'

   
        
    