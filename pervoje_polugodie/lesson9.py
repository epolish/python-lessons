# Форматирование строк с помощью метода (функции) format

print('Hello, {}!'.format('Vasya'))

print('{0}, {1}, {2}'.format('a', 'b', 'c'))

print('{}, {}, {}'.format('a', 'b', 'c'))

print('{2}, {1}, {0}'.format('a', 'b', 'c'))

print('{2}, {1}, {0}'.format(*'abc'))

print('{0}{1}{0}'.format('abra', 'cad'))

print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))

coord = {'latitude': '37.24N', 'longitude': '-115.81W'}

print('Coordinates: {latitude}, {longitude}'.format(**coord))

#--------------------------------------------------------

array = list('список')

for x in array:
    print(x)

for x in range(0, 3):
    print(x)

#--------------------------------------------------------

import random

for x in range(0, random.randrange(0, 10)):
  for x in range(0, random.randrange(0, 100)):
      print('*', end='')
  print()