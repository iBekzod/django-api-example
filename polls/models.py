from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):  
    name = models.CharField(max_length=250)

class Product(models.Model):
    name = models.CharField(max_length=10)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=4,decimal_places=2)
    photo = models.CharField(max_length=1024)

class Customer(models.Model):
    name = models.CharField(max_length=14)
    country = models.CharField(max_length=3)
    address = models.TextField()
    phone = models.CharField(max_length=50)

class Order(models.Model):
    cust_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()

class Detail(models.Model):
    ord_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()

class Invoice(models.Model):
    name = models.CharField(max_length=10)
    ord_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    issued= models.DateField()
    due= models.DateField()
    def is_expired(self):
        now = timezone.now()
        return self.due < now

class Payment(models.Model):
    time = models.DateTimeField()
    amount = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    inv_id = models.ForeignKey(Invoice, on_delete=models.CASCADE)