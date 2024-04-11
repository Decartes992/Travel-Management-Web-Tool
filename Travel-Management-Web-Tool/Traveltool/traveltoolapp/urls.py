from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Route for the home page
    path('about/', views.about, name='about'),  # Route for the about page
    path('contact/', views.contact, name='contact'),  # Route for the contact page
    path('itineraries/', views.itinerary_list, name='itinerary_list'),  # Route for the itinerary list page
    path('itinerary/add/', views.add_itinerary, name='add_itinerary'),  # Route for the add itinerary page
    path('itinerary/<int:pk>/edit/', views.edit_itinerary, name='edit_itinerary'),  # Route for the edit itinerary page, with the itinerary id as a parameter
    path('itinerary/<int:pk>/delete/', views.delete_itinerary, name='delete_itinerary'),  # Route for the delete itinerary page, with the itinerary id as a parameter
]
