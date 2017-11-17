from django.contrib import admin

# Register your models here.
from .models import *





'''
class DeclinaisonInline(admin.TabularInline):
    model = Declinaison
    filter_vertical = ("variantes",)
    extra = 0

class DeclinaisonPriceInline(admin.TabularInline):
    model = DeclinaisonPrice    
    extra = 0
class HouseInline(admin.StackedInline):
    model = House
    extra = 0

class HouseAdmin(admin.ModelAdmin):
    list_display = ('name', )
    inlines = [DeclinaisonInline]


class DeclinaisonAdmin(admin.ModelAdmin):
    list_display = ('house', 'groupe')
    inlines = [DeclinaisonPriceInline]  


'''  

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


