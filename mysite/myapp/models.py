from django.db import models

# Create your models here.
class  Person(models.Model):
   gender_choices={
      ("M","Male"),
      ("F","Female"),
      ("O","Others"),
   }
   
   
   first_name=models.CharField(verbose_name=("person name"),max_length=10)
   middle_name=models.CharField('middle name',max_length=15,blank=True,null=True)
   last_name=models.CharField("Last name",max_length=15)
   email=models.EmailField("Your email")
   gender=models.CharField(max_length=1,choices=gender_choices,default="M")