import utils
import read_csv
import charts


#Llamar el archivo mod que tiene una función que ya hicimos
def run():

  data = read_csv.read_csv('data.csv')
  country = input('Ingrese el pais---> ')
  result = utils.population_by_country(data, country)
  #print(result)

  if len(result) > 0:
    country = result[0]  # Se pone asi para que sea un diccionario lo que salga
    #print(country)
    labels, values = utils.get_population(country)
    #print(labels)
    charts.generate_bar_chart(country['Country/Territory'],labels, values)


if __name__ == '__main__':
  run()
# Si es ejecutado desde la terminal ejecute el metodo run , pero si es eejcutado desde otro archivo no se va eejectuar a menos que se importe con main
