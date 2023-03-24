import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Inicializar FastAPI
app = FastAPI()

# Decorador, donde esta la ruta para ingresar
@app.get('/')
def get_list():
    return[1,2,3]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
    <html>
        <head>
            <title>FastAPI - Test</title>
        </head>
        <body>
            <h1>Hola, esta es una página con HTML!</h1>
        </body>
    </html>
    """


def run():
    store.get_categories()
    
if __name__ == '__main__':
    run()