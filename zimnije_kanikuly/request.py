'''
импортируем библиотеки (внешний код)
json - для кодирования данных
urllib.parse - для преобразования кодировки символов
urllib.request - для организации запросов на удаленный сервер
'''
import json
import urllib.parse
import urllib.request

def check_password(password):
    result = ''
    url = 'http://python-lessons.zzz.com.ua'
    
    '''
    кодируем наши данные
    чтобы кодировка символов у нас на компьютере
    совпадала с кодировкой удаленного сервера
    '''
    data = urllib.parse.urlencode({'password': password}).encode('ascii')

    '''
    with - менеджер контекста
    
    Делаем запрос на удаленный сервер на определенный ранее url
    и с установленными данными
    
    urllib.request.urlopen(url, data)
    '''
    with urllib.request.urlopen(url, data) as response:
        '''
        декодируем ответ от удаленного сервера
        '''
        result = json.loads(response.read().decode('utf-8'))
    
    '''
    возвращаем статус "взлома" пароля
    '''    
    return result['success']