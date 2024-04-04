from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category,Product,Productfile

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display=['parent','title','is_enable','created_time']

class PorductfileInlineAdmin(admin.StackedInline):
    model=Productfile
    fields=['title','file','avatar']
    extra=0


@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):

  list_display=['title','is_enable','created_time']
  inlines=[ PorductfileInlineAdmin]