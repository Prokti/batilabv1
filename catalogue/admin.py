from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

# Register your models here.
from .models import *



class HouseItemInline(admin.TabularInline):
    model = HouseItem
    extra = 1
    

class HouseAttributePriceInline(admin.TabularInline):
    model = HouseAttributePrice
    extra = 1
    

class HouseInline(admin.TabularInline):
    model = House  


#------INTERFACE ADMIN------    

class HouseItemAdmin(admin.ModelAdmin):
    inlines = [HouseAttributePriceInline]
    
    

class HouseAdmin(admin.ModelAdmin):
    list_display = ('name','total', 'groupe')
    fields = ('name', 'price_ht', 'code')
    inlines = [HouseItemInline]



    

admin.site.register(House, HouseAdmin)
admin.site.register(Groupe)
admin.site.register(HouseItem, HouseItemAdmin)
admin.site.register(HouseAttribute)
admin.site.register(HouseAttributePrice)
admin.site.register(HouseAttributeValue)


