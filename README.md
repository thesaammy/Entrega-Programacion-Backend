# Entrega-Programacion-Backend
Proyecto básico curso: PROGRAMACIÓN BACKEND 2025

Estimado profesor, debo admitir que no logre dedicarle el tiempo que me gustaría haberle dedicado a esta entrega, por temas del trabajo que me consumieron horas y animos fuera de horario.

Pese a ello siento que mi proyecto se encuentra completo con algun que otro detalle en el código, algun que otro criterio que quizás no cumpla. Por eso le pido que por favor cualquier tipo de feedback o sugerencia, se lo agradecería.

En el proyecto utilice Docker para la base de datos de prueba para este proyecto, las credenciales se encuentran en el .env (sé que es mala practica pero es por tema de agilizar la entrega del proyecto)

A continuación los detalles de instalación y ejecución de forma breve

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

### 6. Ejecutar con Docker (es necesario tener abierto docker desktop)
```bash
docker-compose up -d
```

### 7. Ejecutar aplicación
```bash
flask run
```

## Acceso
- Aplicación: http://localhost:5000
- Base de datos: Puerto 3306
- Credenciales: Archivo .env
