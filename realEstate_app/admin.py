from django.contrib import admin

from realEstate_app.models import Property


# Register your models here.
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'type_field', 'bathrooms', 'bedrooms', 'size']
    search_fields = ['title', 'type_field']
    list_filter = ['type_field']
