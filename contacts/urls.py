from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('<int:contact_id>', views.single_contact, name='single_contact')
]
