from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'artist', 'label', 'catno', 'format', 'release_id', 'status', 'price', 'listed', 'comments', 'media_condition', 'sleeve_condition', 'accept_offer', 'external_id', 'weight', 'format_quantity', 'location', 'quantity')
    list_filter = ('status', 'media_condition', 'sleeve_condition')
    search_fields = ('title', 'artist', 'label', 'catno', 'comments')

admin.site.register(Listing, ListingAdmin)