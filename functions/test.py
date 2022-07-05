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





# geo_logs = [{'vist2':['Дели','Индия']},{'visit3':['Владимир','Россия']},{'visit9':['Курск','Россия']}]
# print()



# class Class1:
#     def first(self):
#         return 'z '
#     def second(self):
#         return 'z '
# class Class2(Class1):
#     def third(self):
#         return 'z '
#     def fourth(self):
#         return 'z '
# obj = Class2()
# print(obj.first())
# print(obj.second())
# print(obj.third())
# print(obj.fourth())


import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
dis_width = 600
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Pythonist')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
 
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()