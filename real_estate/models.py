from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    email = models.EmailField()


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    c_mobile = models.IntegerField(default=0)
    c_address = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.user.username


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    a_mobile = models.IntegerField(default=0)
    a_address = models.CharField(max_length=200, default='')
    a_company_name = models.CharField(max_length=30, default='')
    a_company_address = models.CharField(max_length=500,  default='')
    a_company_mobile = models.IntegerField( default=0)
    a_company_email = models.EmailField( default='')
    a_dis = models.CharField(max_length=500,  default='No description is added')
    a_image = models.FileField(upload_to='images/', null=True, verbose_name="", default='agent-4.jpg')

    def __str__(self):
        return self.user.username


# Property Details
class Property(models.Model):
    # objects = None
    agent = models.ForeignKey(User, on_delete=models.CASCADE)

    type = models.CharField(max_length=100,default='')
    status = models.CharField(max_length=100 , default='')
    description = models.CharField(max_length=500,default='')
    name = models.CharField(max_length=100,default='')
    address = models.CharField(max_length=200,default='')
    area = models.IntegerField(default=0)
    bathroom = models.IntegerField(default=0)
    bedroom = models.IntegerField(default=0)
    masterroom = models.BooleanField("masterroom",default=False,null=True,blank=True)
    balcony = models.BooleanField("balcony", default=False,null=True,blank=True)
    parking = models.BooleanField("parking", default=False,null=True,blank=True)
    lift = models.BooleanField("lift", default=False,null=True,blank=True)
    storeroom = models.BooleanField("storeroom", default=False,null=True,blank=True)
    swimming = models.BooleanField("swimming", default=False,null=True,blank=True)
    builder = models.CharField(max_length=100,default='')
    price = models.IntegerField(default=0)
    image = models.FileField(upload_to='images/', null=True, verbose_name="", default='')

    def __str__(self):
        return self.name


class Afeedback(models.Model):
    subject=models.CharField(max_length=100, default='')
    description= models.TextField( default='')

    def __str__(self):
        return self.subject


class Ufeedback(models.Model):
    subject=models.CharField(max_length=100, default='')
    description=models.TextField( default='')

    def __str__(self):
            return self.subject


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/', null=True, blank=True)

    def __str__(self):
        return self.property.name


class Comments_model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='')
    u_email = models.EmailField(max_length=100, default='')
    comments = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name

