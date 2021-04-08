
from .import models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, Customer, Agent

x= forms.TextInput(attrs={'class':"form-control"})
y= forms.NumberInput(attrs={'class':"form-control"})
z= forms.CheckboxInput(attrs={})
a = forms.FileInput(attrs={'class':"form-control"})


class PropertyDetails(forms.ModelForm):
    name = forms.CharField(required=True, widget=x)
    type = forms.CharField(required=True, widget=x)
    address = forms.CharField(required=True, widget=x)
    status = forms.CharField(required=True, widget=x)
    builder = forms.CharField(required=True, widget=x)
    description = forms.CharField(required=True, widget=x)
    area = forms.IntegerField(required=True, widget=y)
    bathroom = forms.IntegerField(required=True, widget=y)
    bedroom = forms.IntegerField(required=True, widget=y)
    price = forms.IntegerField(required=True, widget=y)
    lift = forms.BooleanField(widget=z,  required=False)
    parking = forms.BooleanField(widget=z, required=False)
    storeroom = forms.BooleanField(widget=z, required=False)
    masterroom = forms.BooleanField(widget=z, required=False)
    balcony = forms.BooleanField(widget=z, required=False)
    swimming = forms.BooleanField(widget=z, required=False)
    image = forms.FileField(required=True, widget=a)

    class Meta:
        model = models.Property
        fields = ['status','lift','swimming','storeroom','description','type', 'name', 'address', 'area', 'bathroom', 'bedroom', 'parking', 'masterroom', 'price', 'builder', 'balcony', 'image']


class PropertyImageForm(forms.ModelForm):
    images = forms.FileField(required=False)

    class Meta:
        model = models.PropertyImage
        fields = ('images',)


class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    c_mobile = forms.IntegerField(required=True)
    c_address = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.c_mobile = self.cleaned_data.get('c_mobile')
        customer.c_address = self.cleaned_data.get('c_address')

        customer.save()
        return user


x2 = forms.TextInput(attrs={'class':"form-control"})


class AgentSignUpForm(UserCreationForm):
    username = forms.CharField(required=True, widget=x2)
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':"form-control"}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':"form-control"}))
    first_name = forms.CharField(required=True, widget=x2)
    last_name = forms.CharField(required=True, widget=x2)
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':"form-control"}))

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_agent = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        agent = Agent.objects.create(user=user)
        agent.save()
        return user


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


x1 = forms.TextInput(attrs={'class':"form-control"})


class Agent_profile(forms.ModelForm):
    a_mobile = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class':"form-control"}))
    a_address = forms.CharField(required=True, widget=x1)
    a_company_name = forms.CharField(required=True, widget=x1)
    a_company_address = forms.CharField(required=True, widget=x1)
    a_dis = forms.CharField(required=True, widget=x1)
    a_company_mobile = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class':"form-control"}))
    a_company_email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':"form-control"}))
    a_image = forms.FileField(required=True, widget=forms.FileInput(attrs={'class':"form-control"}))

    class Meta:
        model = models.Agent
        fields = ['a_mobile', 'a_address', 'a_company_name', 'a_company_address', 'a_company_mobile', 'a_company_email', 'a_image']


# class Comment_form(forms.ModelForm):
#     name = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class': "form-control form-control-lg form-control-a", 'placeholder':"Name"}))
#     u_email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': "form-control form-control-lg form-control-a", 'placeholder':"Email"}))
#     comments = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control form-control-lg form-control-a", 'placeholder':"Comments"}))
#
#     class Meta:
#         model = models.Agent
#         fields = ['name', 'u_email', 'comments']
