from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from . models import All_equipment

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




class EquipmentForm(ModelForm):

    assigned_to = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
   

    class Meta:
         model= All_equipment
         fields = [
            'assigned_to'
            #'asset_no', 
            #'device_type',
            #'device_make',
            #'device_model', 
            #'location_status', 
            #'serial_no', 
            #'purchase_reason',
            #'price',
            #'in_service',
            #'image', 
            #'date_assigned',
         ]
