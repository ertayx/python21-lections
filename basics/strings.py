"================Строки==============="

# строки - неизменяемый тип данных, который предназначен для хранения текста или же последовательности символов, заключенного в одинарные или двойные ковычки

# Синтаксис:

string1 = 'строка с одинарными ковычками' 

string2 = "строка с двойными ковычками"

# error = 'не правильная строка"

string3 = "don't" # внутри двойных ковычек все одинарные - просто символы

string4 = '"makers"'# внутри одинарные ковычек все двойных - просто символы

string5 = '''
многострочный текст 
в одинарных ковычках
тут можно ставить "любые"
'ковычки'
'''
string6 = """
многострочный текст 
в двойных ковычках
тут можно ставить "любые"
'ковычки'
"""


"================Экранизация строк================="

# экранизация спец-символов

'\n'#перенос на новою строку

'\t'#табуляция

'\\'#отображается \

'\''#отображение '

'\"'#отображение "

'\r'#возвращение коретки в начало строки

'\v'#перенос на новою строку с смещением в право на длину предыдущей строки

'hello\nworld'
# hello
# world

'hello\tworld'
# hello     world

'чтобы эранировать нужен символ \\'
# чтобы эранировать нужен символ \

'My website is Latracal \rSolution'
# Solutionte is Latracal

'hello\vworld'
# hello
#      world


"==================Форматирование строк==================="
title = 'плов'

price = 1300

format = f'название:{title}, Цена:{price}'

# название:Плов, Цена:1500

format2 = 'название: %s, Цена:%s '

print(format2 %("гуляш", "250"))

print(format2 %("самсы", "70"))

# название:гуляш, Цена:250

# название:самсы, Цена:70

format3 = 'название: {}, цена: {}'

print (format3.format('Шакарап','35'))

# название:Шакарап, Цена:35



"==================Методы строк==================="

# методы типов данных - функции , к которым мы обращяемся через точку

dir(str) # посмотреть все методы класса(типы данных)

'HELLO'.lower() #'hello'

'hello'.lower() #'HELLO'

'Hello'.swapcase() #'hELLO'

'hello'.title() #'Hello'

'hello world'.capitalize()#'Hello world'

'hello'.center(11)#'   hello   ' 

'hello'.center(11, '-')#'---hello---'

'hello'.count('l')# 2 

'hello'.count('ll')# 1

'hello hello'.count('hello')# 2

'hello'.count('w')# 0

'hello world'.startswith('hell')#true

'hello wrold'.endswith('ld')#true

'hello world'.startswith('H')#false


'hello world'.find(5)# 5

'hello world'.find('0')# 4

'hello world'.find('w0')# 6

'hello world'.find('hello')# 0

'hello world'.split()# ['hello', 'world']

'hello world'.split('o')# ['hell','w', 'rld']

'$'.join(['hello', 'world']) # 'hello$world'

' '.join(['hello', 'world']) # 'hello world'

# конкратинация - склеивание строк

'hello' + 'world'#'helloworld'

'hello' +' ' + 'world'#'hello world'





"==================Индексы=================="

# Индекс - это порядковый номер символа в строке

'h e l l o  w o r l d'

#  0 1 2 3 4 5 6 7 8 9 10

string = 'hello world'
string[0]  #'h'
string[10]  #'d'
string[5]  #' '

# срез - подстрока строки

string[0:5]#'hello'
string[0:6]#'hello '
string[2:4]#'ll'

string[:5]#'hello'
string[6:]#'world'
string[:]#'hello world'
string[0:11:2]#'hlowrd'
string[::3]#'hlwl'








"================доп инфа================"

a = 5 
b = 5
print(id(a))
print(id(b))