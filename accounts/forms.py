from django.forms import ModelForm
from .models import House,Owner,Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

WATER = (
        ('Borehole', 'Borehole'),
        ('Pipe', 'Pipe'),
        ('Well', 'Well'),
    )

BATH = (
        ('Personal', 'Personal'),
        ('Shared', 'Shared'),
    )
TYPE = (
        ('Rent', 'Rent'),
        ('Sale', 'Sale'),
        
    )

class HouseForm(ModelForm):
    description = forms.CharField(widget=forms.TextInput(attrs={
        "class":'form-control',
        "placeholder":"Example: 2 Bed room house at... for rent."
    }),label="")
    location = forms.CharField(widget=forms.TextInput(attrs={
        "class":'form-control',
        "placeholder":"location"
    }),label="")
    price = forms.CharField(widget=forms.TextInput(attrs={
        "class":'form-control',
        "placeholder":"Example: Ghc 2000/year"
    }),label="")
    property_type = forms.ChoiceField(choices=TYPE,label="",widget=forms.Select(attrs={'class':'form-control'}))
    contact = forms.CharField(widget=forms.TextInput(attrs={
        "class":'form-control',
        "placeholder":"Contact: 0xxxxxxxxx, 0xxxxxxxxx"
    }),label="")
    available = forms.CheckboxInput()
    rooms = forms.IntegerField(widget=forms.TextInput(attrs={
        "class":'form-control',
        "placeholder":"Number of rooms"
    }),label="")
    bathroom = forms.ChoiceField(choices=BATH,label="Bathroom type: Shared or personal use",widget=forms.Select(attrs={'class':'form-control'}))
    no_of_bathrooms = forms.IntegerField(widget=forms.TextInput(attrs={
        "class":'form-control',
        "placeholder":"Number of bathrooms"
    }),label="")
    furnishes = forms.CharField(widget=forms.Textarea(attrs={
        "class":'form-control',
        "placeholder":"List the furnishes in the house or leave if its an empty apartment"
    }),label="",required=False)
    
    class Meta:
        model = House
        exclude = ['owner','exclusive','hitcount']
      
class ActivationForm(ModelForm):
    class Meta:
        model = User
        fields = ['email']
        widgets = {
            'email': forms.TextInput(attrs={
                'class':'form-control',
                }),
        }


class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        exclude = ['user']
        fields = ['name','email','phone','profile_pic']
        widgets = {
            'name': forms.TextInput(attrs={
                'class':'form-control',
                
                
                }),
            'email': forms.TextInput(attrs={
                'class':'form-control',
                
                
                }),
            'phone': forms.TextInput(attrs={
                'class':'form-control',
                "placeholder":"0xxxxx,0xxxxx,0xxxxx..etc"
                
                
                }),
        }

class CreateUserForm(UserCreationForm):
    
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center'}),
    )

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("the given email is already registered")
        return self.cleaned_data['email']

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class':'form-control',
                
                
                }),
            'email': forms.TextInput(attrs={
                'class':'form-control',
                
                
                }),
        }

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'firstname': forms.TextInput(attrs={
                'class':'form-control',
                
                
                }),
            'lastname': forms.TextInput(attrs={
                'class':'form-control',
                
                
                }),
            'email': forms.TextInput(attrs={
                'class':'form-control',
                
                
                }),
            'message': forms.Textarea(attrs={
                'cols': 30, 'rows': 10,
                'class':'form-control',
                'placeholder':'Type your message'
                
                }),
        }
