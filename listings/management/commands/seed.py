from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")
        
        # Create a sample host user if none exist
        host, created = User.objects.get_or_create(username="host1", defaults={"password": "pass"})
        
        # Sample listings data
        sample_listings = [
            {"title": "Cozy Apartment", "description": "A nice place to stay", "price_per_night": 100.0, "location": "Lagos"},
            {"title": "Beach House", "description": "Close to the beach", "price_per_night": 200.0, "location": "Lekki"},
            {"title": "Mountain Cabin", "description": "Peaceful retreat", "price_per_night": 150.0, "location": "Obudu"},
        ]
        
        for listing_data in sample_listings:
            Listing.objects.create(host=host, **listing_data)
        
        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
