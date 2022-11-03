from django.contrib import admin
from main_food_data.models import Shop
class ShopAdmin(admin.ModelAdmin):
    list_display=('food_title','quntity','Product_name','waight','prise','total','pro_img')
admin.site.register(Shop,ShopAdmin)    
# Register your models here.
