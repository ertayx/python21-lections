# task1
# data = input('введите имя, введите фамилию, введите возраст через пробел:\n').split()
# name = data[0]
# lastname = data[1]
# age = int(data[-1])
# name = name.lower().replace('a', '').title()
# lastname = '*'.join(list(lastname))
# print((name + lastname) * age)

# task2
# b = input('введите строку:').lower()
# a = b.count('a')
# o = b.count('o')
# i = b.count('i')
# e = b.count('e')
# y = b.count('y')
# u = b.count('u')
# print(f'В вашей строке насчитано{a + o + i + e + y + u} гласных букв')

# task3
# a = input('введите ваш юзернейм:')
# center = int(len(a)/2)
# b = a[:center] + '&' + a[center:] + '$'
# password = b.swapcase()

# print(f'вам сгененирован пароль:{password}')


# string = 'hello, world'
# print(string[:])

# string = ('world').find('world')
# print(string)
# string = 'The quick brown fox jumps over the lazy dog'
# c = string.replace('o', '*')
# print(c)
# string = 'hello'
# a = 'h'
# b = 'o'
# string1=string[-4:] [0:3]
# string2 = b + string1 + a
# print(string2)
# string = 'tree'
# string1=string[-1:] + string[1:-1] + string[:1]
# print(string1)
# hashtags = '#makers#bootcamp#программирование#it#курсы'
# x = hashtags.lstrip('#')
# print(x.split('#'))
# name = input()
# last_name = input()
# age = input()
# city = input()
# print(f'Вас зовут: {name} {last_name}, Ваш возраст:{age}, Вы \nпроживаете в городе {city}')
# string = 'abracadabra'
# string1 = 'abracadabra'
# center = int(len(string)/2)
# center1 = int(len(string)/2)
# b = string[:center] 
# c = string[center1:] 
# c1 = c[1:] 
# print(b + 'K' + c1) 
# string = input()
# newString = (string[1:-1])
# print(string[-1]+newString+string[0])



# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print(f'{i} FizzBuzz')
#     elif i % 5 == 0:
#         print (f'{i}Buzz')
#     elif i % 3  == 0:
#         print(f'{i}Fizz')
#     else:
#         print(i)



# x=1
# y=2
# z=3
# if x>z and y>z:
#    print(z)
# elif x<y and x<z:
#     print(x)
# else:
#     print(y)

# x = int(input()) 
# y = int(input())
# c = x//y 
# d = x%y
# if x%y==0:
#     print('x не делится на y')
#     print(f'Частное: {c}')
#     print(f'Остаток: {d}')
# else:
#     print('x делится на y')
#     print(f'Частное: {c}')
#     print(f'Остаток: {d}')


# a1= input()
# a = list(a1)
# counter = 0
# qwerty1 = 0
# if len(a) > 8 and any([x.isdigit() for x in a1]) and any([x.isupper() for x in a1]):
#     qwerty1 += 1
# qwerty = 'qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролджэячсмитьбю'
# for i in range(len(a) - 2):
#     if a1[i:i + 3].lower() in qwerty:
#         break
#     else:
#         counter = + 1
# if int(counter) + int(qwerty1) == 2:
#     print('ok')
# else:
#     print('error')

# task1
# password = input('Придумайте пароль:')
# if password.isdigit() and len(password) >= 8:
#     print('Ваш пароль сохранен')
# if not password.isdigit():
#     print('Ваш пароль должен хранить только числа')
# if not len(password) >= 8:
#     print('Ваш пароль должен содержать не менее 8 символов')

# task2
# math = int(input('введите ваш балл по математике: '))
# engl = int(input('введите ваш балл по английскому: '))
# litr = int(input('введите ваш балл по литературе: '))
# c = (math + engl + litr)/3
# if c > 69:
#     print(f'Вы допущены к экзаменам. Ваш средний балл составляет{round(c, 1)}')
# else:
#     print(f'Вы не допущены к экзаменам. Ваш средний балл составляет{round(c, 1)} .Проходной балл выше 50')
# import random
# user = input("Сделайте выбор — камень, ножницы или бумага: ")
# possible = ["камень", "бумага", "ножницы"]
# computer = random.choice(possible)
# if user == computer:
#     print(f"Оба пользователя выбрали {user}. Ничья!!")
# elif user == "камень":
#     if computer == "ножницы":
#         print("Камень выигрывает ножницы! Вы победили!")
#     else:
#         print("Бумага выигрывает камень! Вы проиграли.")
# elif user == "бумага":
#     if computer == "камень":
#         print("Бумага выигрывает камень! Вы победили!")
#     else:
#         print("Ножницы выигрывает бумагу! Вы проиграли.")
# elif user == "ножницы":
#     if computer == "бумага":
#         print("Ножницы выигрывает бумагу! Вы победили!")
#     else:
#         print("Камень выигрывает ножницы! Вы проиграли.")
# import string
# num = int(input())
# book = chr(num)
# if book in string.punctuation + string.digits:
#     print(f'Это не буква, а символ "{book}"')
# else:
#     print(f'Это буква "{book}"')
# count = '0'
# number = input()
# if number.isnumeric():
#     count = number
#     print(count)
# else:
#     print(count)
# a = [1, 'xyi', True, 8.9]
# for n in a:
#     print(n)
# name_of_list = 'jopaa'
# new_list = list(name_of_list[round(len(name_of_list) / 2):] + name_of_list[:round(len(name_of_list) // 2)])
# print(new_list)
# list_ = ['world', 'hello'] 
# new_list = len(list_)//2
# print(new_list) 
# a = {'x': 1, 'y': 2, 'z': 1}

# print(a = dict.fromkeys[1])

# a = {'x': 1, 'y': 2, 'z': 1}
# b = list(a.keys())
# print(a[2])




# x = float(input('Введите возраст в человеческих годах: '))
# if x == 1:
#   print('вашему псу:',10.5 / 2,'собачьих лет')
# elif x == 2:
#   print('вашему псу: 10.5 собачьих лет')
# elif x > 2:
#   print('вашему псу:',x * 4+2.5,'собачьих лет')


# x = int(input('Количество гостей:'))
# gosti = {}
# for i in range(1,x+1):
#     y = input('Введите имена гостей:')
#     gosti.setdefault(i, y)
# print(gosti)

# x = {1: 'a', 2: 'b', 3: 'c'}
# y = {}
# for key, val in x.items():
#   y.update({val: key})
#   y % 2
# print(y)

# spisok = [
#     {'картошка': 5},
#     {'огурец': 6},
#     {'банан': 4}
# ]
# while spisok:
#     jjj = input()
#     for i in spisok:
#         if jjj in i:
#             del i[jjj]
#             print(spisok)
#     if not any (spisok):
#         break
# print('время платить ')

# list_ = [1,2,3,2,3,4,1,23,4]
# while list_:
#     list_.remove(2)
#     print(list_)
# list_ = ['world', 'hello'] 
# new_list = list_[::-1]
# print(new_list)

nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for res in nums:
    if res < 5:
        print(list(filter(res)))
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# print(list(filter(lambda elem: elem < 5, a)))