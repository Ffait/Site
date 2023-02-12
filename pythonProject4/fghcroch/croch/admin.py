from django.contrib import admin

from .models import Products, Category


class ProductsAdmin (admin.ModelAdmin):
    list_display = ('name', 'price', 'cat')
    list_display_links = ('name',)
    search_fields = ('name', )
    list_editable = ('cat', 'price')
    list_filter = ('price', )
    prepopulated_fields = {"slug": ("name", )}


class CategoryAdmin (admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )
    search_fields = ('name', )
    prepopulated_fields = {"slug": ("name", )}


admin.site.register(Products, ProductsAdmin,)
admin.site.register(Category, CategoryAdmin)
