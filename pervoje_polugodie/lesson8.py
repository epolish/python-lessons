# пример создания своих функций

#без параметра (аргумента)
def do_something():
    print('something')

#с параметром с заранее заданным значением (аргументом)
def formatted_print(count=10):
    print('-' * count)

#с несколькими параметрами (аргументами)
def my_super_function(first_number, second_number):
    return first_number + second_number

do_something()
formatted_print()
formatted_print(90)
my_super_function(5, 7)

###############################################################

a = 5
b = 6

if (a > b):
    print('a > b')
elif (a < b):
    print('a < b')
else:
    print('a == b')

a, b = 6, 5

if (a > b):
    print('a > b')
elif (a < b):
    print('a < b')
else:
    print('a == b')

a = 6
b = 6

if a > b:
    print('a > b')
elif a < b:
    print('a < b')
else:
    print('a == b')

# TODO: переписать код с использованием функций