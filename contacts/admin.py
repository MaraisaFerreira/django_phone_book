from django.contrib import admin
from .models import Category, Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',
                    'phone_number', 'email', 'created_at', 'category')

    list_display_links = ('first_name', 'last_name')
    list_filter = ('category',)
    list_per_page = 50

    search_fields = ('first_name', 'last_name', 'phone_number', 'email')


admin.site.register(Category)
admin.site.register(Contact, ContactAdmin)
