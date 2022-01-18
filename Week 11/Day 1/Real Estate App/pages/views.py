from django.shortcuts import render
from listings.choices import bedroom_choices, state_choices, price_choices

from listings.models import Listings
from realtors.models import Realtor

def index(request):
    listings = Listings.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'states_choices': state_choices,
        'bedrooms_choices': bedroom_choices,
        'prices_choices': price_choices,
    }
    return render(request, "listings.html", context)


def about(request):
    #get all the realtors
    realtors = Realtor.objects.get_order_by('hire_date')
    #get  MVP
    mvp_realtor = Realtor.objects.all().filter(is_mpv=True)
    context = {
        'realtors': realtors,
        'mvp_realtor':mvp_realtor,
    }

    return render(request, 'about.html')