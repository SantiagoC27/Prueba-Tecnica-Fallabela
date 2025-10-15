# 🏦 Falabella Client App

Aplicación de **prueba técnica** desarrollada con:

- **Backend:** Flask (Python)
- **Frontend:** Angular
- **Base de datos:** SQLite (archivo separado)

---

## 🚀 Puesta en producción

### 🧩 Backend (Flask)

Se recomienda usar **Waitress** como servidor WSGI en producción.

Instalación de Waitress:

```bash
pip install waitress

waitress-serve --listen=0.0.0.0:5000 app:app
```

### 💻 Frontend (Angular)

```bash
ng build --prod
```

## ☁️ Despliegue

Puedes usar plataformas como:

- Render

- Railway

- AWS EC2

- Azure App Service

- Google Cloud Run

Sube el backend (Flask) como API REST.

Sube los archivos estáticos del frontend (carpeta /dist).

Configura las variables de entorno y conexión con la base de datos SQLite.