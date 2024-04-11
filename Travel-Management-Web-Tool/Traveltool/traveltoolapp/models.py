"""
File: models.py
Author: Iftekhar Rafi
Dal ID: B00871031

This file contains the implementation of the classes used in the Travel Itinerary Planning and Management Tool.

Classes:
- Destination: Represents the travel destination with city and country.
- Hotel: Stores details of the hotel for the trip.
- Itinerary: Stores and manages details of a travel itinerary.
"""

from django.db import models

# Destination Model
class Destination(models.Model):
    """
    Represents the travel destination with city and country.
    Fields:
    - city: The city of the travel destination.
    - country: The country of the travel destination.
    """
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.city}, {self.country}"


# Hotel Model
class Hotel(models.Model):
    """
    Stores details of the hotel for the trip.
    Fields:
    - name: The name of the hotel.
    - address: The address of the hotel.
    """
    name = models.CharField(max_length=200, default="None")
    address = models.CharField(max_length=200, default="None")

    def __str__(self):
        return f"{self.name}, {self.address}"


# Itinerary Model
class Itinerary(models.Model):
    """
    Stores and manages details of a travel itinerary.
    Fields:
    - destination: A foreign key that links to the Destination model.
    - departure_date: The departure date of the trip.
    - return_date: The return date of the trip.
    - hotel: A foreign key that links to the Hotel model.
    """
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    departure_date = models.DateField()
    return_date = models.DateField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def get_summary(self):
        """
        Returns a dictionary containing a summary of the itinerary.
        """
        return {
            "destination": str(self.destination),
            "departure_date": self.departure_date,
            "return_date": self.return_date,
            "hotel": str(self.hotel),
        }

    def __str__(self):
        itinerary_summary = self.get_summary()
        return f"Itinerary for {itinerary_summary['destination']} from {itinerary_summary['departure_date']} to {itinerary_summary['return_date']}"
