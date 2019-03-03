from django.contrib import admin

from .models import Realtor

# Register your models here.

#Customize admin data showing
class RealtorAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'email', 'hire_date')
    list_display_links=('id', 'name')
    search_fields=('email',)
    list_per_page=25

admin.site.register(Realtor, RealtorAdmin)