from django import forms

class EmpForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Full Name'}))
    Email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}))
    Password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}))
    PhoneNo=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Your Phone number'}))