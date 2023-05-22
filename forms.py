from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm


class ApplyForm(ModelForm):
    class Meta:
        model=Candidates
        fields="__all__"
        
class RegisterForm(UserCreationForm):    
    class Meta:
        model=User
        fields="__all__"
        
# class CompanyForm(ModelForm):    
#     class Meta:
#         model=Company
#         fields="__all__"
        
