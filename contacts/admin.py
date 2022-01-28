from django.contrib import admin
from .models import Category, Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',
                    'phone_number', 'email', 'created_at', 'category',
                    'is_visible')

    list_display_links = ('first_name', 'last_name')
    list_filter = ('category',)
    list_per_page = 25

    search_fields = ('first_name', 'last_name', 'phone_number', 'email')
    list_editable = ('phone_number', 'is_visible')


admin.site.register(Category)
admin.site.register(Contact, ContactAdmin)
