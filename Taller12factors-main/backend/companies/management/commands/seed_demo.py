from django.core.management.base import BaseCommand
from datetime import datetime, timezone
from companies.mongo import companies_collection, material_listings_collection


class Command(BaseCommand):
    help = "Crea datos demo en MongoDB"

    def handle(self, *args, **kwargs):
        existing = companies_collection.find_one({"nit": "900000001"})

        if not existing:
            result = companies_collection.insert_one({
                "owner_uid": "demo-owner",
                "name": "EcoRed Demo",
                "nit": "900000001",
                "city": "Bogotá",
                "sector": "Manufactura",
                "created_at": datetime.now(timezone.utc).isoformat(),
            })

            material_listings_collection.insert_one({
                "company_id": result.inserted_id,
                "material_type": "Cartón",
                "quantity": 80,
                "unit": "kg",
                "location": "Bogotá",
                "status": "available",
                "published_by": "demo-owner",
                "created_at": datetime.now(timezone.utc).isoformat(),
            })

        self.stdout.write(self.style.SUCCESS("Datos demo creados en MongoDB"))
