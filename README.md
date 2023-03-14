# Steps

## Python course PIP

This is a repository of the course of PIP and virtual enviroments using concepts of previous courses

## Game Project

Para correr el juego "Piedra, papel, tijera" es necesario seguir las siguientes instrucciones en la Terminal:

```sh
cd game
python3 main.py
```

## App Project

Para correr el proyecto de "Obtener gráficas de población de un país" es necesario seguir las siguientes instrucciones en la Terminal, donde se recomienda tener WSL o Ubuntu para mayor facilidad:

```sh
git clone
cd app
source env/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

**Nota:** Es necesario crear la carpeta **"imgs"** dentro de la carpeta del proyecto App, para evitar errores al momento de la ejecución. También se recomenda crear el entorno virtual después de clonar el repositorio de la siguiente forma:

```sh
python3 -m venv env
```