#форматы записи чисел
very_big_number = 1000000000
very_big_number = 1_000_000_000

#bool - функция преобразования параметра (передаваемого значения) в логический тип (True - False)
print(bool())
print(bool(1))
print(bool(-1))
print(bool(0))
print(bool('1'))
print(bool('0'))
print(bool(''))

#float - функция преобразования параметра (передаваемого значения) в число с плавающей запятой (дробное)
print(float('45'))
print(float('45.456'))
print(float(45.455555555555555555))
print(float('ASD45.456')) # тут будет ошибка - python не может конвертировать эту строку в дробное число

#int - функция преобразования параметра (передаваемого значения) в целое число
print(int('45'))
print(int(True))
print(int(False))
print(int('45.456')) # тут будет ошибка - python не может конвертировать эту строку в целое число
print(int(45.455555555555555555))
print(int('ASD45.456')) # тут будет ошибка - python не может конвертировать эту строку в целое число

#abs - модуль числа (absolute)
print(abs(7))
print(abs(-7))

#print - вывод значения на экран
print('print')

#type - определение типа переменной
print(type(True))
print(type('str'))
print(type(4.5))
print(type(0))

#help - интересная функция
help()