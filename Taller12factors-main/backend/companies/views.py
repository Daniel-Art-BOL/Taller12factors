from datetime import datetime, timezone
from bson import ObjectId
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from companies.mongo import companies_collection, material_listings_collection

class CompanyViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        # CORRECCIÓN: Usamos request.user.username (donde guardamos el email)
        uid = request.user.username 
        companies = list(
            companies_collection.find(
                {"owner_uid": uid},
                {
                    "owner_uid": 1,
                    "name": 1,
                    "nit": 1,
                    "city": 1,
                    "sector": 1,
                    "created_at": 1,
                },
            )
        )

        for company in companies:
            company["id"] = str(company["_id"])
            del company["_id"]

        return Response(companies)

    def create(self, request):
        # CORRECCIÓN: Usamos request.user.username
        uid = request.user.username 
        data = request.data

        document = {
            "owner_uid": uid,
            "name": data.get("name"),
            "nit": data.get("nit"),
            "city": data.get("city"),
            "sector": data.get("sector"),
            "created_at": datetime.now(timezone.utc).isoformat(),
        }

        result = companies_collection.insert_one(document)
        return Response({"id": str(result.inserted_id)}, status=status.HTTP_201_CREATED)


class MaterialListingViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        # CORRECCIÓN: Usamos request.user.username
        uid = request.user.username 
        companies = list(companies_collection.find({"owner_uid": uid}, {"_id": 1}))
        company_ids = [company["_id"] for company in companies]
        items = list(material_listings_collection.find({"company_id": {"$in": company_ids}}))

        for item in items:
            item["id"] = str(item["_id"])
            item["company_id"] = str(item["company_id"])
            del item["_id"]

        return Response(items)

    def create(self, request):
        data = request.data
        document = {
            "company_id": ObjectId(data.get("company_id")),
            "material_type": data.get("material_type"),
            "quantity": float(data.get("quantity")),
            "unit": data.get("unit", "kg"),
            "location": data.get("location"),
            "status": data.get("status", "available"),
            # CORRECCIÓN: Usamos request.user.username
            "published_by": request.user.username,
            "created_at": datetime.now(timezone.utc).isoformat(),
        }

        result = material_listings_collection.insert_one(document)
        return Response({"id": str(result.inserted_id)}, status=status.HTTP_201_CREATED)


@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def health(request):
    return Response({"status": "ok"})