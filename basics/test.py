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
# if i % 3 == 0 and i % 5 == 0:
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
# new_list = list(name_of_list[round(len(name_of_list) // 2 ):] )
# new_list1 = list(name_of_list[:round(len(name_of_list) // 2 + 1)])
# new_list2 = new_list + new_list1
# print(new_list2)
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
# while 2 in list_:
#     list_.remove(2)
#     print(list_)
    
# list_ = ['world', 'hello'] 
# new_list = list_[::-1]
# print(new_list)

# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for res in nums:
#     if res < 5:
#         print(list(map(res)))
# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# res = list(filter(lambda elem: elem < 5, nums))
# print(res)

# list_ = list(input())
# tuple_ = list_
# print(tuple(tuple_))
# print(tuple_)

# new = input()
# list_ = new.split(',')
# tuple_ = tuple(list_)
# print(list_)
# print(tuple_)

# list_ = [1, 2, 3, 4,]
# for new_list in list_:
#     print(str(new_list))

# list_ = [1, 2, 3]
# new_list = [str(x) for x in list_]
# print (new_list)


# list_ = ['1', '2', '3', '4', '5']
# for i in range(list_):
#     if i % 2 == 0 :
#         print('четное')
#     elif i % 2 !=  0:
#         print ('нечетное')


# captains = ['Janeway', 'Picard', 'Sisko']
 
# for i in range(len(captains)):
#     if 

# string = 'HelloWorld!'
# string1 = 'HelloWorld!'
# center = int(len(string)/2)
# center1 = int(len(string)/2)
# b = string[:center] 
# c = string[center1:] 
# print(b + 'K' + c) 

# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
# for b in a.values():
#     if a % 2 != 0:
#         print(b)
# list_ = [1, 2, 3, 4, 5]
# for b in list_:
#     if b % 2 == 0:
#         b.update()
# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25} 
# temp = dict()
# for key in a:
#     temp[key] = a[key] / 5
# print(temp)

# a = {'a': 1, 'b': 2, 'c': 3} 
# for k,v in a.items():
#     print(v[::-1],k[::-1])

# a = {'a': 1, 'b': 2, 'c': 3} 
# b = {}
# for k,v in a.items():
#     b.update({v: k})
# print(b)

# a = {'a': 3, 'b': 2}
# b = sum(a.values())
# print(b)

# a1 = {'a':1}
# a2 = dict(a = 2)
# a3 = dict([("Russia", "Moscow")])

# string = "pythonist" 
# b = list(string)
# dict_ = dict.fromkeys(b, 1)
# for i in dict_.keys():
#     if i == 2:
#         dict_+1
# print(dict_)

# str1 = 'pythonist'
# my_dict = {i: str1.count(i) for i in str1}
# print(my_dict)


# list_ = [1, 2, 3, 4, 5]
# new_list = []
# for i in list_:
#     if i % 2 == 0:
#         new_list.append('четное')
#     else:
#         new_list.append('нечетное')
# print(new_list)

# list_ =  [1, 2, 3]
# if list_:
#   list_ = [1,2,3]
# if (list_.count([0]) < 1) or (list_.count([1]) < 1) or (list_.count([2]) < 3):
#     print('yes')
# else:
#     print('ERROR')

# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# new_list = [i for i in len(list_name) if i >= 4 ]
# print(new_list)

# dict_ = {1: None, 2: None, 3: None, 4: None, 5: 'efrfe', 6: None, 7: None, 8: None, 9: None, 10: None}
# newdict = {k: k**2 for k in dict_.keys()}
# print((newdict))
# print(list(dict_.keys()))

# dict_ = {k: k**2 for k in  range(1,11)}
# print(dict_)

# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# new_list = [ 'shorter' if len(i) <=4 else 'longer' for i in list_name]
# print(new_list)

# n = int(input())
# dict_ = {i: i*i  for i in range(1,501) if i%9==0 }
# print(dict_)

# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {
#     key : list(range(1, value + 1))
#     for key, value in a.items() 
# }
# print(dict_)

# dict_ = {'first': 1, 'second': 2, 'third': 3}
# a = { key: 'even' if  values % 2==0 else 'odd' for key, values in dict_.items() }
# print(a)

# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list_ = [list1 for list1 in str.split(string_) if list1.isdigit()]
# print(list_)

# dict_ = {
#     'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
#     'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
#     'Nik': {'history': 84, 'math': 85, 'literature': 87}
#     }
# new_dict = {key:
#     str(list(({inner_key: inner_value for inner_key, inner_value in value.items() if inner_value == max(list(value.values()))}).keys())).lstrip("['").rstrip("]'")
#     for key, value in dict_.items()}
# print(new_dict)

# lst = [8, 2, 6, 4, 3, 1, 10]

# # Filter all elements <8
# small = [x for x in lst if x < 8]
# print(lst)
# print(small)

# a = input()
# b = ['a','e','y','u','i','o']
# ab = [len(item) for item in a if b in a ]
# print(ab)

# print(len([1 for x in list(input()) if x in ['a', 'e', 'i', 'o', 'u', 'y']]))

# my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
# dict_ = {key: val2 for key, val in my_dict.items() for val2 in val.values()}
# print(dict_)

# list_ = [float(i//2) for i in range(0,11) if i %2==0]
# print(list_)

# dict_ = {1:'a', 2:'bar', 3:'c'}
# n = {key: len(key) for key in dict_.keys()if key%2==0 }
# print(n)

# x = {1:'aasda'}
# b = list(x.values())
# c = b.pop()
# print(str(len(c)))

# dict_ = {1:'a', 2:'bro', 3:'re'}
# res = {key:len(val) **3 if key % 2!=0 else len(val) for key,val in dict_.items()  }
# print(res)

# dict_ = {1: 'hello', 2: {'makers': 2, 'bootcamp': 4}, 'makers': 6, 3: 'bootcamp'}
# res = {
#     key if type(key) == int else val
#     : 
#     val if type(val) != dict else {val2: key2 for key2, val2 in val.items()}
#     for key, val in dict_.items()
# }
# print(res)

# set1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# set2 = {8, 9, 10, 11, 12, 13, 14, 15, 16, 17}
# full_set = {set.union(set1,set2)}
# i = 'В этом сете было 3 повторения, его длина составляет 17'
# x = { i for i in full_set if full_set<20 }
# print(full_set)

# from random import shuffle
# sa = list(range(1,21))
# sb = list(range(1,21))
# shuffle(sa)
# shuffle(sb)
# a = {sa.pop() for _ in range(10)}
# b = {sb.pop() for _ in range(10)}
# ab = a | b
# n = len(ab)
# print(ab)
# print(f'В этом сете было {20-n} повторения, его длина составляет {n}')

# set1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# set2 = {8, 9, 10, 11, 12, 13, 14, 15, 16, 17}
# full_set = set.union(set1,set2)
# n = len(full_set)
# print(full_set)
# print(f'В этом сете было {20-n} повторения, его длина составляет {n}')

# try:
#     age = int(input())
#     if age<18:
#         raise ValueError('Доступ запрещён')
# except:
#     print('Введён некорректный возраст')  
# else:
#     print('Спасибо')

# finally:
#     print('До свидания!')

# try:
#     cash = int(input())
#     if cash<0:
#         raise ValueError('Сумма не может быть отрицательной!')
#     print(cash) 
# except Exception as e:
#     print(e)
     

# try:
#     cash = int(input('Сумма в бумажнике? '))
#     if cash < 0: raise
# except ValueError:
#     print('Ожидается ввод числа')
# except:
#     print('Сумма не может быть отрицательной!')

# cash = int(input())
# if cash<0:
#     raise ValueError('Сумма не может быть отрицательной!')
# else:
#     print(cash)

# try:
#     inp1 = input()
#     inp2 = input()
#     if type(int(inp1))  == int and type(int(inp2)) == int:
#         print(int(inp1)+int(inp2))  
# except:
#      if type(str(inp1))  == str and type(str(inp2)) == str:
#         print(str(inp1)+str(inp2))  


# inp1 = input()
# list_ = []
# for t in inp1.split():
#     try:
#         list_.append(float(t))
#     except ValueError:
#         pass
#         raise('Данный элемент не является числом!') 
# print(list_)

# for i in a:
#     b.append(i)
#     if i == str:
        
#         print('Данный элемент не является числом')
#     print(i.isdigit())
#     print(b.append(i))


inp1 = input()

list_ = []
for t in inp1.split():
    try:
        list_.append(float(t))
    except Exception as e:
        raise e('Данный элемент не является числом!')
    else:
        print(list_)
print(list_)
 

# inp1 = input()

# list_ = []
# for t in inp1.split():
#     try:
#         list_.append(float(t))
#     except :
#          raise ValueError('Данный элемент не является числом!')
#     else:
#         print(list_)
# print(list_)


# inp1 = input()
# try:
#     list_ = [list1 for list1 in str.split(inp1) if list1.isdigit()]
# except ValueError:
#     print("Данный элемент не является числом")
# print(list_)


# list_ = list(range(0,101))
# newlist = []
# for i in list_:
#     if i % 2==0:
#         newlist.append(i)
# print(newlist)