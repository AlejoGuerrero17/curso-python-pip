import csv
import re


def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(
      reader)  # Me saca la primera fila el encabezado al hacer esto
    # cuando se ejcuta el for evitamos que se lea siempre el encabezado
    #print(header)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
      data_2 = []
    for a in data:
      for k in a.values():
        if k == 'Argentina':
          salida = {
            key: value
            for key, value in a.items() if re.search('.... Population', key)
          }
          data_2.append(salida)

    pais = list(
      filter(lambda item: item['Country/Territory'] == 'Argentina', data))
    print(pais)
    '''
    data_2 = []
    for a in data:
      c = {
        key: value
        for (key, value) in a.items() if re.search('.... Population', key)
      }
      data_2.append(c)
    print(data_2[0])
    '''


if __name__ == '__main__':
  a = read_csv('./app/data.csv')
