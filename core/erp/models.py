from django.db import models
from datetime import datetime

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')

    
    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['id']


class Employee(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    dni = models.CharField(max_length=15, unique=True, verbose_name='dni')
    name = models.CharField(max_length=150, verbose_name='Nombres')
    addres = models.TextField(null=True, blank=  True)
    age = models.PositiveIntegerField(default=0)
    sex = models.CharField(max_length=10) 
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True)
    cvitae = models.FileField(upload_to='cvitae', null=True, blank=True)
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    date_creation = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table ='empleado'