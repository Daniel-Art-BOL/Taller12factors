import os
from pymongo import MongoClient
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DB_NAME = os.getenv("MONGODB_DB_NAME", "ecored_circular_db")

client = MongoClient(MONGODB_URI)
db = client[MONGODB_DB_NAME]

companies_collection = db["companies"]
material_listings_collection = db["material_listings"]
