from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import All_equipment
from django.forms.widgets import NumberInput

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={"class":"form-control"}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']



class EquipmentForm(forms.ModelForm):
        class Meta:
         model= All_equipment
         fields = [
            'asset_no',
            'device_type',
            'device_make',
            'device_model', 
            'location_status', 
            'serial_no', 
            'purchase_reason',
            'price',
            'in_service',
            'image',
            'date_assigned',
            'assigned_to'

         ]



        assigned_to = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
        device_type = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
        device_make = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
        device_model = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
        location_status = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
        serial_no = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
        purchase_reason = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
        date_assigned = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    
    