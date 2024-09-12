from django.contrib import admin
from .models import *

# Register your models here.
class productData(admin.ModelAdmin):
    list_display=['product_name','product_price','product_img','product_model','product_ram']

admin.site.register(product_master)
admin.site.register(sub_category,productData)