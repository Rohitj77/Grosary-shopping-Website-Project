from distutils.command.upload import upload
from email.policy import default
from django.db import models

#from django import forms
class Shop(models.Model):
     #main_food=models.CharField(max_length=100,null=True,blank=True)
     food_title=models.CharField(max_length=100,null=True,blank=True)
     quntity=models.IntegerField(default=1)
     Product_name=models.CharField(max_length=100,null=True)
     waight= models.CharField(max_length=100,null=True)
     prise= models.IntegerField(null=True)
     total= models.IntegerField(blank=True,null=True)
     pro_img=models.FileField(upload_to="shop",max_length=250,null=True,default=None)

     def line_total(self):
        return self.quntity * self.prise
     """total_pri=quntity*prise
     total_prise= models.IntegerField(total_pri,null=True)
     def __init__(self,qun,pri):
      self.quntity=qun
      self.prise=pri
     def total_prise(self):
      total=self.quntity*self.prise
t=Shop(quntity,prise) 



   



# Create your models here.
class Thing(models.Model):
  PRIORITIES = (
    (0, 'Low'),
    (1, 'Normal'),
    (2, 'High'),
  )

  priority = models.IntegerField(default=0, choices=PRIORITIES)"""