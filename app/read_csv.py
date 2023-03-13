# Modulo para lectura de archivos .CSV
import csv

def read_csv(path):
  # Solo se va a leer el archivos
  with open(path, 'r') as csvfile:
  # Delimitador => Normalmente viene separados por , o por ;
    reader = csv.reader(csvfile, delimiter = ',')
    
    # Cada una de las columnas viene en forma de listas
    # Toca transformarlo como un array de diccionarios
    
    # Obtener el nombre de las columnas => iterar manualmente
    header = next(reader)
    # print(header)
    data = []
    # Lectura de cada fila => 
    for row in reader:
      # Usar un zip para unir header/row => Queda como tuplas
      iterable = zip(header,row)
      # Generar un dict con dictionary comprehension
      country_dict = {key:value for key, value in iterable}
      # print(country_dict)
      data.append(country_dict)
      #print('***' * 5)
      #print(row)
    return data

# Ejecucion del script
if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])

