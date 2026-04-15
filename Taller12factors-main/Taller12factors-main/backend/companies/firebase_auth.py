import os
import firebase_admin
from firebase_admin import credentials, auth
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")
cred_path = os.getenv("FIREBASE_CREDENTIALS_PATH")

# Inicializar Firebase solo cuando se necesite
_firebase_app = None

def _get_firebase_app():
    global _firebase_app
    if _firebase_app is None:
        if not firebase_admin._apps:
            cred = credentials.Certificate(cred_path)
            _firebase_app = firebase_admin.initialize_app(cred)
        else:
            _firebase_app = firebase_admin.get_app()
    return _firebase_app


class FirebaseAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return None

        if not auth_header.startswith("Bearer "):
            raise exceptions.AuthenticationFailed("Token mal formado")

        id_token = auth_header.split("Bearer ")[1]

        try:
            # Asegurar que Firebase esté inicializado
            _get_firebase_app()
            decoded_token = auth.verify_id_token(id_token)
            request.firebase_user = decoded_token
            return (None, None)
        except Exception:
            raise exceptions.AuthenticationFailed("Token inválido")
            decoded_token = auth.verify_id_token(id_token)
            request.firebase_user = decoded_token
            return (None, None)
        except Exception:
            raise exceptions.AuthenticationFailed("Token inválido")
