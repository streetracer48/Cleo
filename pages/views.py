from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import state_choices, bedroom_choices, price_choices

# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:6]

    context = {
        'listings':listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices':price_choices
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