from django.contrib import admin


from .models import *

class CategoriesAdmin(admin.ModelAdmin):
    thumbnail = ('thumbnail')  # List of fields to make read-only

class ProductsAdmin(admin.ModelAdmin):
    thumbnail = ('thumbnail')  # List of fields to make read-only

class ImageAdmin(admin.ModelAdmin):
    model = Pro_images
    list_display = ['img_title','image_tag']

admin.site.register(Categories,CategoriesAdmin)
admin.site.register(Products,ProductsAdmin)
admin.site.register(Pro_images,ImageAdmin)