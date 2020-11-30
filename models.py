from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ("Pending","Pending"),
    ("Out of dilivery","Out of dilivery"),
    ("Dilivered","Dilivered")
)

CATEGORY_CHOICES =(
    ("indoor","indoor"),
    ("outdoor","ourdoor")
)

class  Customer(models.Model):
    user = models.OneToOneField(User,null = True , on_delete=models.CASCADE)
    name = models.CharField(max_length=200 ,null=True)
    phone = models.CharField(max_length=10 ,null=True)
    profile_img = models.ImageField(default="logo.jpg" ,null=True,blank=True)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=256,null=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    name= models.CharField(max_length=200 ,null=True)
    price = models.FloatField()
    category = models.CharField(max_length=200,choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=500 ,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=256,choices=STATUS_CHOICES)
    note = models.CharField(max_length=300,null=True)

    def __str__(self):
        return f"{self.customer} - {self.product}"


class Daily_Q(models.Model):
    date = models.DateField(auto_now_add=True)
    description = models.TextField()
