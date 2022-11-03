from django.db import models
class Ptital(models.Model):
    main_food=models.CharField(max_length=100,null=True,blank=True)

# Create your models here.
