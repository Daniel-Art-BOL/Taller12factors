import os
import firebase_admin
from firebase_admin import credentials, auth
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

# --- MEJORA: Ruta absoluta para evitar el 403 ---
cred_path = os.getenv("FIREBASE_CREDENTIALS_PATH")
if cred_path and not os.path.isabs(cred_path):
    cred_path = os.path.join(BASE_DIR, cred_path)

_firebase_app = None

def _get_firebase_app():
    global _firebase_app
    if _firebase_app is None:
        if not firebase_admin._apps:
            # Verificación de existencia del archivo
            if not os.path.exists(cred_path):
                print(f"ERROR CRÍTICO: No se encuentra el archivo en {cred_path}")
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
            return None # No lanzamos error aquí para permitir peticiones públicas si existen

        id_token = auth_header.split("Bearer ")[1]

        try:
            _get_firebase_app()
            # Verificación del token con Firebase
            decoded_token = auth.verify_id_token(id_token)
            
            # --- CORRECCIÓN CLAVE ---
            # Django REST necesita un objeto de usuario, creamos uno ficticio con los datos de Firebase
            from django.contrib.auth.models import User
            user, _ = User.objects.get_or_create(
                username=decoded_token['email'],
                email=decoded_token['email']
            )
            
            return (user, None)
        except Exception as e:
            print(f"Error de autenticación Firebase: {e}")
            raise exceptions.AuthenticationFailed(f"Token inválido: {str(e)}")