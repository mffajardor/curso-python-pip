# Charts
# Matplotlib no viene incluido en las librerias principales de Python
# Instalarlo por packages de Replit

# Para no colocarle todo el nombre "matplotlib.pyplot" => Se coloca un alias => as 
import matplotlib.pyplot as plt

def generate_bar_chart(name, labels,values): 
  # Figura, coordenadas
  # print("labels =>",labels)
  # print("values =>",values)
  fig, ax = plt.subplots() # Debe estar vacio
  # Generar una gráfica de barras
  ax.bar(labels, values)
  plt.savefig(f'./imgs/{name}.png')
  plt.close()

def generate_pie_chart(labels,values):
  # Figura, coordenadas
  fig, ax = plt.subplots() # Debe estar vacio
  # Generar el pie => Labels se debe escribir así
  ax.pie(values, labels = labels)
  ax.axis('equal') # Se genere en el centro
  plt.savefig('pie.png')
  plt.close()
  
# Ejecutar el script (como archivo)

  if __name__ == '__main__':
    labels = ['a','b','c']
    values = [10, 40, 80]
    # generate_bar_chart(labels,values)
    generate_pie_chart(labels,values)
