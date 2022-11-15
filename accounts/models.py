from django.db import models
from django.contrib.auth.models import User

class customer(models.Model):
    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=200, null=True)
    phone=models.CharField(max_length=200, null=True)
    email=models.CharField(max_length=200, null=True)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class products(models.Model):
    CATEGORY=(
        ('Indoor','Indoor'),
        ('Outdoor','Outdoor')
    )
    name=models.CharField(max_length=200, null=True)
    price=models.FloatField()
    category=models.CharField(max_length=200, null=True, choices=CATEGORY)
    description=models.CharField(max_length=200, null=True)
    date_created=models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class tag(models.Model):
    tname=models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.tname

class order(models.Model):
    STATUS=(
        ('Pending','Pending'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered','Delivered')
    )
    customer=models.ForeignKey(customer, null=True, on_delete=models.SET_NULL)
    product=models.ForeignKey(products, null=True, on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    status=models.CharField(max_length=200, null=True, choices=STATUS)
    tags=models.ManyToManyField(tag)

    def __str__(self):
        return self.status
