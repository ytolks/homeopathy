from django.shortcuts import render
from django.shortcuts import render
from .models import Listing
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.shortcuts import get_object_or_404
#  from listings.choices import price_choices,bedroom_choices,state_choices
# Create your views here.

def index(request):
    
    listings = Listing.objects.order_by('-list_date')
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)
   

# def listing(request,listing_id):
def listing(request,listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {'listing': listing }
    return render(request, 'listings/listing.html',context)
   

def search(request):
    # get all listings from database
    query_set_list = Listing.objects.order_by('-list_date')


    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_set_list = query_set_list.filter(homeopathy_name__istartswith=keywords,)

#city - starts with 

    # if 'city' in request.GET:
    #     keywords = request.GET['city']
    #     if keywords:
    #         query_set_list = query_set_list.filter(city__istartswith=keywords)

#State
    # if 'state' in request.GET:
    #     keywords = request.GET['state']
    #     if keywords:
    #         query_set_list = query_set_list.filter(state__iexact=keywords,)

#Bedrooms
    # if 'bedrooms' in request.GET:
    #     keywords = request.GET['bedrooms']
    #     if keywords:
    #         query_set_list = query_set_list.filter(bedrooms__lte=keywords,)

#Price
    # if 'price' in request.GET:
    #     keywords = request.GET['price']
    #     if keywords:
    #         query_set_list = query_set_list.filter(price__lte=keywords,)
    context  = {

       
        'listings': query_set_list,
    

    }
    # return render(request, 'listings/search.html',context)
    return render(request, 'listings/search.html',context)
# Create your views here.
