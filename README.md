# Entrega-Programacion-Backend
Proyecto básico curso: PROGRAMACIÓN BACKEND 2025

## Requisitos
- Python 3.8+
- Docker
- Docker Compose

## Instalación

### 1. Instalar Python
- Descargar desde [python.org](https://www.python.org/downloads/)
- Verificar instalación: `python --version`

### 2. Instalar Docker
- Descargar desde [docker.com](https://www.docker.com/get-started)
- Verificar instalación: `docker --version`

### 3. Clonar el repositorio
```bash
git clone <URL_DEL_REPOSITORIO>
cd Entrega-Programacion-Backend
```

### 4. Configurar entorno virtual
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 5. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 6. Ejecutar con Docker
```bash
docker-compose up -d
```

### 7. Ejecutar aplicación
```bash
python app.py
```

## Acceso
- Aplicación: http://localhost:5000
- Base de datos: Puerto 3306
- Credenciales: Archivo .env
