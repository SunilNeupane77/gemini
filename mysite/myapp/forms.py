from django import forms

class UserForm(forms.Form):
   first_name=forms.CharField(max_length=10,min_length=2)
   middle_name=forms.CharField(max_length=10,min_length=2,required=False)
   last_name=forms.CharField(max_length=10,min_length=2)
   