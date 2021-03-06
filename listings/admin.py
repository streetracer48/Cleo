from django.contrib import admin

from .models import Listing

# Register your models here.


#Customize admin data manipulation and showing

class ListingAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links=('id', 'title')
    list_filter=('realtor',)
    list_editable=('is_published',)
    search_fields=('title', 'description', 'address', 'zipcode', 'city', 'state', 'price')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)
