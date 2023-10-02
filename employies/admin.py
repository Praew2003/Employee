from django.contrib import admin

# Register your models here.

from .models import Department, Information

@admin.register(Department)
class Admin(admin.ModelAdmin):
    list_display = ("department",)
    search_fields = ("department",)
    
@admin.register(Information)
class MajorAdmin(admin.ModelAdmin):
    list_display = (
        'fname', 
        'lname', 
        'gender',
        'age',
        'elevel',
        'department',
)
    