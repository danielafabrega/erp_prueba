from django.db import models
from django.utils import timezone
from datetime import date


# Create your models here.

class Supplier(models.Model):
    supplier_id = models.CharField(max_length=200) 
    name = models.CharField(max_length=200)
    business_name = models.TextField()
    address = models.TextField()
    city = models.TextField()
    email = models.EmailField(max_length=200)
    phone = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Product(models.Model):
    product_code = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    cost = models.IntegerField(default=0)
    purchase_date = models.DateTimeField(default=timezone.now)
    stock = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    def __str__(self):
        return self.product_code
 
class Booksale(models.Model):
    #incorporar año/mes separar meses de venta
    month_year = models.DateField(default=date.today)
    sales_date = models.DateTimeField(default=timezone.now)
    document_type = models.CharField(max_length=200,default="Factura electrónica")
    price = models.IntegerField(default=0)
    neto_price = models.IntegerField(default=0)
    iva = models.IntegerField(default=19)
    total_price = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    m_pay = models.CharField(max_length=200, default="Efectivo")
    def __str__(self):
        return str(self.month_year)


class Kardex(models.Model):
    code = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    document_type = models.CharField(max_length=200)
    number = models.AutoField(primary_key=True)
    price = models.IntegerField(default=0)
    debe = models.IntegerField(default=0)
    haber = models.IntegerField(default=0)
    def __str__(self):
        return self.code


class Customer(models.Model):
    customer_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    address = models.TextField()
    email = models.EmailField(max_length=200)
    phone = models.IntegerField(default=0)
    def __str__(self):
        return self.customer_id


    

