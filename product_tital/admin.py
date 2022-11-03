from django.contrib import admin
from product_tital.models import Ptital
class PtitalAdmin(admin.ModelAdmin):
    list_display=('main_food',)
admin.site.register(Ptital,PtitalAdmin)    




 

# Register your models here.
