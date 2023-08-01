from django.contrib import admin

# Register your models here.
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','homeopathy_name','potency_30','potency_200','potency_1m','potency_ml1','description')
    list_display_links = ('id','homeopathy_name',)
    list_filter = ('homeopathy_name',)
    list_editable = ('potency_30','potency_200','potency_1m','potency_ml1','description')
    search_fields = ('homeopathy_name','potency_30','potency_200','potency_1m','potency_ml1','description',)
    list_per_page = 10

admin.site.register(Listing, ListingAdmin)