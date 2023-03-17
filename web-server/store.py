import requests

api_url_categories = 'https://api.escuelajs.co/api/v1/categories'

def get_categories():
    # Obtener los tipos de productos de la API
    r = requests.get(api_url_categories)
    print(f'Status code: {r.status_code}')
    print(f'Text of API: {r.text}')
    print(f'Type of data: {type(r.text)}')
    
    # Convirtiendo el dato de Str a JSON => Manipular como diccionario
    categories = r.json()
    
    # Iterar cada una de las categorias
    values = [category['name'] for category in categories]
    print(values)
    