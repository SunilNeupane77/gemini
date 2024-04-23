from django import forms

class UserForm(forms.Form):
   first_name=forms.CharField(max_length=10,min_length=2)
   middle_name=forms.CharField(max_length=10,min_length=2,required=False)
   last_name=forms.CharField(max_length=10,min_length=2)
   
class PayementForm(forms.Form):
   first_name=forms.CharField(max_length=12,min_length=5)
   middle_name=forms.EmailField(max_length=45,min_length=12,required=True)  
   