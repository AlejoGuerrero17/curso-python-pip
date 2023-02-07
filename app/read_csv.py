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
    return data


'''
datos = []
g = ['X', 'X1', 'X2', 'X3', 'X4']
x = 1
for m in range(1, 100):
  d = list(zip(g, range(x, x + 4)))
  x += 4
  my_dict = {key: value for key, value in d}
  datos.append(my_dict)

lista = list(filter(lambda valor: valor['X1'] > 80, datos))
print(lista)
'''
if __name__ == '__main__':
  a = read_csv('./app/data.csv')
