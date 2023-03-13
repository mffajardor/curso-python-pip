# Archivo utils.py Función para obtener la población de un país
# Función
def get_population(country_dict):
  # Seleccionar las columnas
  population_dict = {
    '2022': int(country_dict['2022 Population']),
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),
    '2010': int(country_dict['2010 Population']),
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population']),
  }

  # Return debe ser un array de los valores y uno de los labels
  labels = list(population_dict.keys())
  # print("labels =>",labels)
  values = list(population_dict.values())
  # print("values =>",values)
  return labels, values

# Variable
#A = 'Hola'

# 2 Parametros: DAta - Una lista y Coutry - El país
def population_by_country(data, country):
  # Recibo una lista con diccionarios
  # Selecciono el diccionario con el país que tenga esa lista
  result = list(filter(lambda item: item['Country'] == country, data))
  return result

'''
# Como va a estar el diccionario
[
  {
  'Country': 'Colombia',
  'Population': 300   
  }
  {
  'Country': 'Bolivia',
  'Population': 200   
  }
  
]
'''