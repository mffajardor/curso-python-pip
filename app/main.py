# Archivo Main.py - Donde se llaman los módulos
# Para llamar el modulo => Con import se hace
import utils
import read_csv
import charts


def run():

  data = read_csv.read_csv('data.csv')

  # Se puede filtrar la data por los continentes
  data = list(filter(lambda item: item['Continent'] =='South America',data))
  countries = list(map(lambda x: x['Country'], data))

  percentages = list(map(lambda x: float(x['World Population Percentage']), data))

  charts.generate_pie_chart(countries, percentages)
  
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