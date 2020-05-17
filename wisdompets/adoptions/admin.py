from django.contrib import admin

# Register your models herefrom
from .models import Pet

@admin.register(Pet)

class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'species','breed','age','sex']
