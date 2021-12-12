from django.contrib import admin

class ProductAdminModel(admin.ModelAdmin):
    search_fields=('name', 'number', 'off', 'added_in', 'price')