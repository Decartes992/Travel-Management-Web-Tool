from django.shortcuts import render, get_object_or_404, redirect
from .models import Itinerary, Destination, Hotel

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")

def itinerary_list(request):
    itineraries = Itinerary.objects.all()
    return render(request, 'itinerary.html', {'itineraries': itineraries})

def add_itinerary(request):
    if request.method == 'POST':
        # Get the form data from the request
        city = request.POST.get('city')
        country = request.POST.get('country')
        departure_date = request.POST.get('departure_date')
        return_date = request.POST.get('return_date')
        hotel_name = request.POST.get('hotel_name')
        hotel_address = request.POST.get('hotel_address')

        # Create a Destination object
        destination = Destination(city=city, country=country)
        destination.save()

        # Create a Hotel object
        hotel = Hotel(name=hotel_name, address=hotel_address)
        hotel.save()

        # Create an Itinerary object
        itinerary = Itinerary(destination=destination, departure_date=departure_date, return_date=return_date, hotel=hotel)
        itinerary.save()

        # Redirect to the itinerary_list view
        return redirect('itinerary_list')

    # Render the form
    return render(request, 'add_itinerary.html')

def edit_itinerary(request, pk):
    itinerary = get_object_or_404(Itinerary, pk=pk)
    if request.method == "POST":
        # Get the form data from the request
        city = request.POST.get('city')
        country = request.POST.get('country')
        departure_date = request.POST.get('departure_date')
        return_date = request.POST.get('return_date')
        hotel_name = request.POST.get('hotel_name')
        hotel_address = request.POST.get('hotel_address')

        # Update the Destination object
        itinerary.destination.city = city
        itinerary.destination.country = country
        itinerary.destination.save()

        # Update the Hotel object
        itinerary.hotel.name = hotel_name
        itinerary.hotel.address = hotel_address
        itinerary.hotel.save()

        # Update the Itinerary object
        itinerary.departure_date = departure_date
        itinerary.return_date = return_date
        itinerary.save()

        # Redirect to the itinerary_list view
        return redirect('itinerary_list')

    # Render the form
    return render(request, 'edit_itinerary.html', {'itinerary': itinerary})


def delete_itinerary(request, pk):
    itinerary = get_object_or_404(Itinerary, pk=pk)
    if request.method == "POST":
        itinerary.delete()
        return redirect('itinerary_list')
    return render(request, 'delete_itinerary.html', {'itinerary': itinerary})
