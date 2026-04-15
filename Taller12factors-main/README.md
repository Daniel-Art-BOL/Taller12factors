# Taller 1 — EcoRed Circular

Aplicación cloud-native mínima con **React**, **Django REST Framework**, **Firebase Authentication** y **MongoDB Atlas**, orientada a evidenciar rigurosamente los principios de **Twelve-Factor App**.

## Video de apoyo

[▶ Ver video](https://uniempresarial-my.sharepoint.com/:v:/g/personal/abeltran_uniempresarial_edu_co/IQBgLxQxE0NVSJV0fggITaXLAYKDKrG24zrSsFEI8c1u8tw?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D&e=Ay98Ym)

## Navegación del taller

### A. Caso de estudio
[Ir a la sección A](docs/A-caso-de-estudio.md)

### B. Configuración de backing services
[Ir a la sección B](docs/B-backing-services.md)

### C. Creación de backend
[Ir a la sección C](docs/C-backend.md)

### D. Creación de frontend
[Ir a la sección D](docs/D-frontend.md)

### E. Despliegue local
[Ir a la sección E](docs/E-despliegue-local.md)

---

## Alcance del taller

Este taller se concentra en una arquitectura mínima funcional alrededor del **módulo de empresas** del caso de estudio **EcoRed Circular**.

El énfasis del taller **no está en evaluar amplitud funcional**, sino en verificar la correcta aplicación de los **12 factores** a lo largo de todas las secciones:

- codebase
- dependencias
- configuración
- backing services
- build, release y run
- procesos
- port binding
- concurrencia
- disposability
- paridad entre ambientes
- logs
- procesos administrativos

## Resultado esperado

Al finalizar, cada equipo debe dejar funcionando:

- un repositorio único con `backend/`, `frontend/` y `docs/`,
- backend Django REST conectado a MongoDB Atlas,
- frontend React autenticando con Firebase,
- registro de empresas,
- registro de publicaciones asociadas a empresa,
- consulta de información registrada,
- documentación explícita de evidencias Twelve-Factor distribuida transversalmente en todas las secciones.

## Versión del taller

La entrega actual corresponde a la **versión 1.0**.

Esto significa que el proyecto se encuentra en su primer estado liberado y documentado. En futuras iteraciones podrán aparecer nuevas versiones, por ejemplo `v2.0` o `v2.1`, sin crear otro proyecto ni duplicar el repositorio.

Es importante diferenciar:

- **versión**: estado liberado del código, por ejemplo `v1.0` o `v2.0`
- **ambiente**: contexto donde esa versión se ejecuta, por ejemplo `dev`, `test` o `prod`

La misma versión puede pasar por varios ambientes. Si `v1.0` se encuentra en pruebas, el equipo puede continuar nuevos desarrollos hacia una versión futura, pero sin alterar automáticamente la versión congelada que está siendo validada.

## Estructura general del repositorio

```text
ecored-circular/
├── backend/
├── frontend/
├── docs/
│   ├── A-caso-de-estudio.md
│   ├── B-backing-services.md
│   ├── C-backend.md
│   ├── D-frontend.md
│   └── E-despliegue-local.md
└── README.md
```

---

## Estado del Proyecto ✅ COMPLETADO

**Fecha de finalización:** Abril 2026  
**Versión:** 1.0  
**Estado:** Funcional y listo para despliegue

### ✅ Componentes Implementados

#### Backend (Django REST Framework)
- ✅ Autenticación Firebase integrada
- ✅ Conexión MongoDB Atlas configurada
- ✅ API REST para empresas y materiales
- ✅ Modelo de datos completo
- ✅ Configuración de 12 factores aplicada
- ✅ Servidor ejecutándose en puerto 8000

#### Frontend (React + Vite)
- ✅ Autenticación Firebase
- ✅ Interfaz de login
- ✅ Gestión de empresas (CRUD)
- ✅ Gestión de materiales
- ✅ Navegación protegida por autenticación
- ✅ Diseño responsive con CSS personalizado

#### Infraestructura
- ✅ Repositorio Git conectado a GitHub
- ✅ Variables de entorno configuradas
- ✅ Documentación completa
- ✅ Datos de demostración incluidos

### 🚀 Instrucciones de Despliegue Local

#### Prerrequisitos
- Python 3.11+
- Node.js 18+
- Git
- Cuenta Firebase
- MongoDB Atlas

#### 1. Clonar el repositorio
```bash
git clone https://github.com/Daniel-Art-BOL/Taller12factors.git
cd Taller12factors
```

#### 2. Configurar Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

Configurar variables de entorno en `.env`:
```env
FIREBASE_SERVICE_ACCOUNT_KEY_PATH=path/to/serviceAccountKey.json
MONGODB_URI=your_mongodb_atlas_uri
DJANGO_SETTINGS_MODULE=config.settings
```

```bash
python manage.py seed_demo  # Cargar datos de ejemplo
python manage.py runserver
```

#### 3. Configurar Frontend
```bash
cd ../frontend
npm install
```

Configurar variables de entorno en `.env`:
```env
VITE_FIREBASE_API_KEY=your_firebase_api_key
VITE_FIREBASE_AUTH_DOMAIN=your_project.firebaseapp.com
VITE_FIREBASE_PROJECT_ID=your_project_id
VITE_API_BASE_URL=http://localhost:8000/api
```

```bash
npm run dev
```

#### 4. Acceder a la aplicación
- **Backend API:** http://localhost:8000/api/health
- **Frontend:** http://localhost:5173
- **Documentación:** Ver carpeta `docs/`

### 🔐 Configuración de Servicios Externos

#### Firebase Authentication
1. Crear proyecto en Firebase Console
2. Habilitar Authentication con Email/Password
3. Generar Service Account Key (para backend)
4. Obtener configuración web (para frontend)

#### MongoDB Atlas
1. Crear cluster en MongoDB Atlas
2. Configurar usuario de base de datos
3. Obtener connection string
4. Configurar IP whitelist (0.0.0.0/0 para desarrollo)

### 📋 Verificación de 12 Factores

Cada sección de la documentación (`docs/`) incluye evidencia específica de cumplimiento de los 12 factores aplicados en este proyecto.

### 🐛 Solución de Problemas

- **Error de espacio en disco:** El proyecto está optimizado para funcionar con dependencias mínimas
- **Error de autenticación:** Verificar credenciales de Firebase y MongoDB
- **Error de conexión:** Verificar variables de entorno y configuración de red

---

**Proyecto desarrollado como parte del Taller 12 Factores - EcoRed Circular**
