# Archivo Main.py - Donde se llaman los módulos
# Para llamar el modulo => Con import se hace
import utils
import read_csv
import charts
import pandas as pd


def run():
  # Utilizando pandas para facilitar uso
  
  df = pd.read_csv('data.csv')
  
  # Similar a: data = list(filter(lambda item: item['Continent'] =='South America',data))
  df = df[df['Continent'] == 'Africa'] 
  
  # Equivale a: countries = list(map(lambda x: x['Country'], data))
  countries = df['Country'].values
  
  # Equivale a: percentages = list(map(lambda x: float(x['World Population Percentage']), data))
  percentages = df['World Population Percentage'].values
  
  charts.generate_pie_chart(countries, percentages)
  
  
  data = read_csv.read_csv('data.csv')
  country = input("Type a country => ")
  print(country)
  print("=== Info del país ===")
  result = utils.population_by_country(data,country)
  
  if len(result) > 0:
    country = result[0]
    print(country)
    labels,values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'],labels,values)

# Ejecutar el como Scripts directamente desde la terminal
if __name__ == '__main__':
  run()