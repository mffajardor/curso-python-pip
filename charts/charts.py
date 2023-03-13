import matplotlib.pyplot as plt

# Funcion para generar un pie chart
def generate_pie_chart():
    labels = ['A','B','C']
    values = [200, 34, 120]
    
    # Creando una figura con subplots => Coordenadas
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()