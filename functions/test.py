# task 3
# dict_ = {
#     'ar':3,
#     'ma':4,
#     'ba':5,
#     'sh': 6,
# }
# def dictionary(dict_):
#     for x in dict_.keys():
#         print(x) 
# dictionary(dict_)

# task 7
# def is_palindrome(p):
#     if p[::-1].lower() == p.lower():
#         return True
#     else:
#         return False
# print(is_palindrome('Mom'))

# task 8
# def max_num(a,b):
#     if a > b:
#         return a
#     elif b > a:
#         return b
# print(max_num(10,12))

# task 9
# def multiply_list(a):
#     answer = 1
#     for i in a:
#         answer *= i
#     return answer
# print(multiply_list([1,2,3,4,5,6]))

# формула преобразования
# a = 105
# b = list(str(a))
# c = [int(x) for x in b]
# print(sum(c))

# task 10
# def sum_digits(a):
#     b = list(str(a))
#     c = [int(x) for x in b]
#     return sum(c)
# sum_digits(105) 

# classwork 1
# import random
# def generate_password(a, b):
#     ran = random.sample(range(1, 11), k=7)
#     ran = [str(i) for i in ran]
#     res = a + b + ''.join(ran)
#     return res
# def get_info(name = input(),pas = input()):
#     res = generate_password(a = name, b = pas)
#     return res
# print(get_info())

# classwork 2
# def get_data():
#     x = int(input('выберите первое число:'))
#     y = int(input('выберите второе число:'))
#     z = input('выберите операцию: + , - , * , // :')
#     if z == '+':
#         print(x+y)
#     elif z == '-':
#         print(x-y)
#     elif z == '*':
#         print(x*y)
#     elif z == '//':
#         print(x//y)
#     else:
#         print('не гоните опастно для жизни')
# get_data()

# def plus(a, b):
#     return a + b
# def delen(a,b):
#     return a / b
# def proiz(a,b):
#     return a * b
# def minus(a,b):
#     return a - b
# print('1 плюс')
# print('2 деление')
# print('3 Умножение')
# print('4 Миинус')

# value = input('Выбери от 1 до 4: ')
# val1 = int(input('выберите первое число:'))
# val2 = int(input('выберите втовое число:'))
# if value == '1':
#     print(plus(val1, val2))
# elif value == '2':
#     print(delen(val1, val2))
# elif value == '3':
#     print(proiz(val1, val2))
# elif value == '4':
#     print(minus(val1, val2))
# else:
#     print('я смотрю ты опасный чел')

# def factorial(n):
#     res = 1
#     for i in range(1, n + 1):
#         res *= i
#     return res

# print(factorial(3))
# print(factorial(5))

# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# b = {}
# for k,v in list(a.items()):
#     if v % 2 == 0:
#         b.update({k:2})
#     else:
#         b.update({k:v})
# print(b)

# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# for v in a.copy():
#     if a[v] == None:
#         a.pop(v)
# print(a)

# a = {'a': 1, 'b': 2, 'c': 3}
# b = {k: v for v,k in a.items()}
# print(b)
# answer = 1
# lis = [1,2,3,4,5]
# for i in lis:
#     answer *= i 
# print(answer)

# string = 'pythonistiyt'
# z = list(string)
# x = {v: string.count(v) for v in list(z)}
# print(x)

# task 2
# x = 'Я глобальная переменная!'
# print(x)  
# def my_func():
#     global x 
#     x = 'Я могу измениться'
#     print(x)
# my_func()
# print(globals())

# task 4
# balance = 0
# def get_salary(amount):
#     global balance
#     balance += amount
# def pay_bills(amount,log_name):
#     global balance
#     balance -= amount
#     print(f'Вы заплатили {amount} сом за {log_name}')
# def get_balance():
#     global balance
#     print(f'У вас на счету {balance} сом')
# get_salary(1000)
# get_balance()
# pay_bills(400,'xui')
# get_balance()

# task 6
# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}
# def club():
#     global a
#     for k,v in a.items():
#         if v < 17:
#             print(f'{k},извините, Вы не проходите по age-control')
#         else:
#             print(f'{k}, Вы можете войти в клуб')
# club()
        
# task 7
# a = ['pipi', 'papa', 'mama']
# b = []
# for x in a:
#     b.append(x.title())
# print(b)

# task 8
# def count_symbols(string):
#     gl = 0
#     sgl = 0
#     sym = 0
#     for x in string.lower():
#         if x in 'уеыаоэяиюё':
#             gl += 1 
#         elif x in 'цкнгшщзмчвфжрлдтспй':
#             sgl +=1
#         else:
#             sym +=1
#     return (f'Количество гласных: {gl}, согласных: {sgl}, остальных символов: {sym}')
# print(count_symbols('хуй'))

# task 9
# a = []
# def zp():
#     global a
#     a.append(range(0,11))
# print(zp())

#task 1 
# list_ = [1,2,3,4]
# result = sum(list_)
# print(result)

# task 9
# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
# list2 = len(list(filter(lambda x: x%2==0,list_)))
# list3 = len(list(filter(lambda x: x%2!=0,list_)))
# result = (f'even: {list2}, odd: {list3}')
# print(result)

# task 10
# from functools import reduce 
# list_ = ['Paul', 'George', 'Ringo', 'John'] 
# result = reduce(lambda x,y: x if  len(x) > len(y) else y,list_)
# print(result)





list_ = [1,2,3,4,5,6,7]
list1 = [i for i in list_ if i%2==0]
print(list1)