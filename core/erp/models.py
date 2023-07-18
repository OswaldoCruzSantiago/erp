from django.db import models
from datetime import datetime

# Create your models here.

class Client(models.Model):
    names  = models.CharField(max_length = 20, verbose_name = "Nombres")
    surnames  = models.CharField(max_length = 20, verbose_name = "Apellidos")
    number = models.CharField(max_length = 20, verbose_name = "Numero")
    email = models.EmailField(max_length=100, verbose_name="Correo")
    age = models.PositiveIntegerField(default = 0, verbose_name = "Edad")
    direction = models.CharField(max_length = 150, verbose_name = "Direccion")
    sex = models.CharField(max_length=70, verbose_name = "Sexo")
    birthday = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')
    

    #Graduacion ojo derecho

    od_sph = models.DecimalField(max_digits = 3, decimal_places = 2, verbose_name = "Esfera")
    od_cyl = models.DecimalField(max_digits = 3, decimal_places = 2, verbose_name = "Cilindro")
    od_axis = models.PositiveIntegerField(max_length= 3, verbose_name = "Eje")
    od_add = models.DecimalField(max_digits = 3, decimal_places = 2,  verbose_name = "Add")
    od_prism = models.DecimalField(max_digits = 3, decimal_places = 2, verbose_name = "Prima")
    od_base = models.DecimalField(max_digits = 3, decimal_places = 2, verbose_name = "Base")
    od_dip = models.CharField(max_length= 6, verbose_name = "Dip")
    od_alt = models.PositiveIntegerField(default=25, verbose_name = "Altura")

    #Graduacion Ojo izquierdo

    oi_sph = models.DecimalField(max_digits = 3, decimal_places = 2, verbose_name = "Esfera")
    oi_cyl = models.DecimalField(max_digits = 3, decimal_places = 2, verbose_name = "Cilindro")
    oi_axis = models.PositiveIntegerField(max_length= 3, verbose_name = "Eje")
    oi_add = models.DecimalField(max_digits = 3, decimal_places = 2,  verbose_name = "Add")
    oi_prism = models.DecimalField(max_digits = 3, decimal_places = 2, verbose_name = "Prisma")
    oi_base = models.DecimalField(max_digits = 3, decimal_places = 2, verbose_name = "Base")
    oi_dip = models.CharField(max_length= 6, verbose_name = "Dip")
    oi_alt = models.PositiveIntegerField(default=25, verbose_name = "Altura")


    def __str__(self):
        return 'Nombre: {}{}'.format(self.names, self.surnames)
    

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table ='cliente'

class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.client.names

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)

    def __str__(self):
        return 'Nombre: {}'.format(self.name)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name = "Nombre", unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']



class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    qty = models.IntegerField(default=1)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        ordering = ['id']

"""
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


"""        