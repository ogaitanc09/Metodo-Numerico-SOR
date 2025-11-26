# Método Numérico SOR - Interfaz Gráfica

Este proyecto implementa el método numérico de **Sobre-Relajación Sucesiva (SOR)**.
El sistema está construido con una arquitectura desacoplada utilizando **Django REST Framework** para el backend (lógica matemática) y **React + Vite** para el frontend (interfaz de usuario).

---

## Guía de Inicio Rápido para Desarrolladores

Sigue estos pasos estrictamente para configurar el entorno de desarrollo en tu máquina local.

### 1. Prerrequisitos
Asegúrate de tener instalado:
* [Git](https://git-scm.com/)
* [Python 3.10+](https://www.python.org/)
* [Node.js](https://nodejs.org/) (versión LTS recomendada)

### 2. Clonar el Repositorio
Abre tu terminal (Git Bash o CMD) y ejecuta en el directorio de tu preferencia:

```bash
git clone https://github.com/ogaitanc09/Metodo-Numerico-SOR.git
cd Metodo-Numerico-SOR
```

### Configuración del Entorno (Solo la primera vez)
Tendrás que configurar el Backend y el Frontend por separado.

### A. Configurar Backend (Django)
1. Entra a la carpeta del backend:
   
```bash
cd  backend
```

3. Crea tu entorno virtual (para no mezclar librerías):
   
```bash
python -m venv venv
```


5. Activa el entorno virtual:
Windows:
```bash
venv\Scripts\activate
```
Mac/Linux:
```bash
source venv/bin/activate
```
(Deberías ver (venv) al inicio de tu línea de comandos).
  
7. Instala las dependencias del proyecto:
   
```bash
pip install -r requirements.txt
```

8. Regresa a la raíz:
   
```bash
cd ..
```
   

### B. Configurar Frontend (React)
1. Entra a la carpeta del frontend:

```bash
cd frontend
```
   
3. Instala las dependencias de Node:
   
```bash
npm install
```

5. Regresa a la raíz:

```bash
cd ..
```

# Ejecutar el Proyecto
Necesitarás abrir dos terminales diferentes (una para Django y otra para React).

### Terminal 1: Backend

```bash
cd backend
# Recuerda activar el entorno si no lo está: venv\Scripts\activate
python manage.py runserver
```


### Terminal 2: Frontend

```bash
cd frontend
npm run dev
```

# Flujo de Trabajo (Git Workflow) - ¡LEER IMPORTANTE!
Para evitar borrar el código:

## 1. Las Ramas (Branches)
* main: PROHIBIDO TOCAR. Es la versión final que se presenta.
* develop: Es nuestra rama base de trabajo. Todo se une aquí primero.

## 2. Cómo empezar una nueva tarea
Nunca trabajes directo en develop. Crea una rama para tu tarea:

### 1. Asegúrate de tener los últimos cambios

```bash
git checkout develop
git pull origin develop
```

### 2. Crea tu rama (usa prefijos: feat/ para mejoras, fix/ para errores)

```bash
git checkout -b feat/nombre-de-tu-tarea
```

### 3. Guardar cambios (Commit)
Haz commits pequeños con mensajes claros:

```bash
git add .
git commit -m "Explicacion del commit"
```


### 4. Subir cambios y Unir (Pull Request)
Cuando termines tu tarea:

Sube tu rama: 
```bash
git push origin feat/nombre-de-tu-tarea
```

Ve a GitHub y crea un Pull Request (PR) hacia la rama develop.

Avísale al equipo para que revisen y aprueben el PR.

# ❌ Lo que NO debes hacer
Nunca subas la carpeta node_modules o la carpeta venv (el .gitignore debería prevenir esto, pero no lo fuerces).

Nunca hagas git push -f (force) a menos que sepas exactamente qué haces.

No trabajes sin antes hacer git pull origin develop para tener lo último que hicieron los demás.
