from django.shortcuts import render, get_object_or_404
from .models import Listings
from django.core.paginator import Paginator
from django.core import paginator


def index(request):
    listings = Listings.objects.order_by('-list_date').filter(is_published=True)
    pagination = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = pagination.get_page(page)
    context = {
        'listings': paged_listings

    }
    return render(request, "listings.html", context)


def listing(request, listing_id):
    #maison = Listings.objects.get(id=listing_id)
    listing = get_object_or_404(pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, "listing.html", context)


def search(request):


def search(request):
  queryset_list = Listing.objects.order_by('-list_date')
    return render(request, "search.html")
  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)

  # City
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      queryset_list = queryset_list.filter(city__iexact=city)

  # State
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
      queryset_list = queryset_list.filter(state__iexact=state)

  # Bedrooms
  if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    if bedrooms:
      queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

  # Price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price)

  context = {
    'state_choices': state_choices,
    'bedroom_choices': bedroom_choices,
    'price_choices': price_choices,
    'listings': queryset_list,
    'values': request.GET
  }

  return render(request, 'listings/search.html', context
