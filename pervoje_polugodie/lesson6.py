# -*- coding: utf-8 -*-

first = input('Vvedite pervoje chislo: ')
second = input('Vvedite vtoroe chislo: ')

if first < second:
  print('pervoe < vtorogo')
elif first > second:
  print('pervoe > vtorogo')
else:
  print('pervoe == vtorogo')

#----------------------------------------

print(True if first == second else False)

#https://pythonworld.ru/osnovy/instrukciya-if-elif-else-proverka-istinnosti-trexmestnoe-vyrazhenie-ifelse.html
#https://pythonworld.ru/osnovy/cikly-for-i-while-operatory-break-i-continue-volshebnoe-slovo-else.html