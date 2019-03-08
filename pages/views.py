from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:6]

    context = {
        'listings':listings
     }
    return render(request, 'pages/index.html', context)

def about(request):
    #GET all realtors

       realtors = Realtor.objects.order_by('hire_date') 
    #GET mvp
       realtor = Realtor.objects.all().filter(is_mvp=True)
       context = {
             'realtors': realtors,
             'mvp_realtors':realtor
                 }
       return render(request, 'pages/about.html', context)