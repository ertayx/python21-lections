# task 3 - inherteins

# class MyString(str):
#     def __init__(self,value):
#         self.value = value
    
#     def __str__(self):
#         return self.value

#     def append(self,string):
#         self.value += string
#         return self.value

#     def pop(self):
#         re = self.value[-1]
#         self.value = self.value[:-1]  
#         return re
    

# example = MyString('String') 
# example.append('hello')
# print(example.pop()) 
# print(example)


# task 4

# class MyDict(dict):
#     def get(self, key, default = 'Are you kidding?'):
#         return dict.get(self, key, default)
# obj_dict = MyDict({'some_title': 2}) 
# print(obj_dict.get('some'))

# task 5

# class Person:
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(f'name:{self.name}, age:{self.age}')
# class Student(Person):
#     def __init__(self,name,age,faculty):
#         super().__init__(name,age)
#         self.faculty = faculty
#     def display_student(self):
#         print(f'name:{self.name}, age:{self.age}, faculty:{self.faculty}')
        
# obj_student = Student('Rick',21,'science')
# obj_student.display() 
# obj_student.display_student() 

# task 6

# class ContactList(list):
#     def __init__(self,list_):
#         self.list_ = list_
#     def search_by_name(self,name):
#         a = []
#         for i in self.list_:
#             if name in i:
#                 a.append(i)
#         return a
# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
# print(all_contacts.search_by_name('Olya')) 

# task 7

# from datetime import datetime
# class SmartPhones:
#     def __init__(self,name,color,memory,battery = 0):
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = 0
#     def __str__(self):
#         return f'{self.name} {self.memory}'
#     def charge(self,per):
#         self.battery = per + self.battery

# class Iphone(SmartPhones):
#     def __init__(self, name, color, memory, ios):
#         super().__init__(name,color,memory)
#         self.ios = ios
#     def send_imessage(self,sending):
#         return f'sending {sending} from {self.name} {self.memory}'

# class Samsung(SmartPhones):
#     def __init__(self,name,color,memory,android):
#         super().__init__(name,color,memory)
#         self.android = android
#     def show_time(self):
#         x = datetime.now().time()
#         return x
# phone = SmartPhones('generic', 'blue', '128GB') 
# print(phone) 
# print(phone.battery) 
# phone.charge(20) 
# print(phone.battery) 
# iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
# print(iphone7)
# print(iphone7.send_imessage('hello')) 
# samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
# print(samsung21.show_time()) 

# task 8

# class CustomError(Exception):
#     def init(self, letters):
#         self.letters = letters

# def check_letters(debil):
#     if debil.isupper():
#         return f'ВСЕ ОТЛИЧНО! {debil}'
#     else:
#         raise capitals_error
    

# capitals_error = CustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')
# print(check_letters('HELLO'))

# task 1 - oop

# class Song:
#     def __init__(self,title,author,year):
#         self.title = title
#         self.author = author
#         self.year = year
#     def show_title(self):
#         print(f'Название этой песни {self.title}')
#     def show_author(self):
#      print(f'Автор этой песни {self.author}')
#     def show_year(self):
#         print(f'Эта песня вышла в {self.year} году')
# song = Song('Happy','Pharrell Williams',2013)
# song.show_title()
# song.show_author()
# song.show_year()

# task 2

# class Circle:
#     color = 'Синий'
#     pi = 3.14
#     def __init__(self,radius):
#         self.radius = radius
#     def get_area(self):
#         return self.pi * (self.radius**2)
# circle = Circle(2) 
# circle.color = 'red'
# print(circle.get_area()) 

# task 3

# class BankAccount:
#     balance = 0    
#     def deposit(self,amount):
#         self.balance = amount + self.balance
#         print(f'Ваш баланс: {self.balance} сом')
#     def withdraw(self,amount):
#         self.balance= self.balance - amount
#         print(f'Ваш баланс: {self.balance} сом')
# account = BankAccount()
# account.deposit(1000) 
# account.withdraw(500) 

# task 4

# class Taxi:
#     def __init__(self,name,cost,cost_km):
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km
#     def get_total_cost(self,km):
#         x = self.cost + self.cost_km * km
#         return f'Такси {self.name}, стоимость поездки: {x} сом'
# taxi1 = Taxi('Namba',45,17)
# taxi2 = Taxi('Yandex',34,23)
# taxi3 = Taxi('Jorgo',79,12)
# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14)) 

# task 5

# class Phone:
#     def __init__(self,name,last_name,phone):
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone
#     def get_info(self):
#         print(f'Контакт: {self.name} {self.last_name}, телефон: +{self.phone}')

# contact = Phone('aibek','basketbolov',123435435)
# contact.get_info()        

# task 6

# class Salary:
#     percent = 8
#     def __init__(self,salary,experience):
#         self.salary = salary
#         self.experience = experience
#     def count_percent(self):
#         x = self.salary / 100 * self.percent
#         return x * self.experience
# obj = Salary(10000,10)
# print(obj.count_percent())

# task 7

# class Nobel:
#     def __init__(self,category,year,winner):
#         self.category = category
#         self.year = year
#         self.winner = winner
#     def get_year(self):
#         x = 2022 - self.year
#         return f'выиграл {x} лет назад'
# winner1 = Nobel("Литература", 1971, "Пабло Неруда") 
# print(winner1.category, winner1.year, winner1.winner) 
# print(winner1.get_year())

  
# winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ") 
# print(winner2.category, winner2.year, winner2.winner) 
# print(winner2.get_year())  

# task 8 

# class Password:
#     def __init__(self, password):
#         self.password = password
#     def __str__(self):
#         pass_ = len(self.password)
#         return pass_ * '*'

#     def validate(self):
#         if len(self.password) < 8 or len(self.password) > 15:
#             raise Exception('Password should be longer than 8, and less than 15')
#         num = list((filter(lambda x: x.isdigit(), self.password)))
#         if len(num) == 0:
#             raise Exception('Password should contain numbers too')
#         string = list((filter(lambda x: x.isalpha(), self.password)))
#         if len(string) == 0:
#             raise Exception('Password should contain letters as well')
#         sym = list(filter(lambda x: x in '@#&$%!~*',self.password ))
#         if len(sym) == 0:
#             raise Exception('Your password should have some symbols')

#         else:
#             return 'Ваш пароль сохранен.'

# password = Password('joe@123456')
# print(password.validate())

# task 9

# from functools import reduce
# class Math:
#     def __init__(self,value):
#         self.value = value

#     def get_factorial(self):
#         list_of_self = list(range(1,self.value +1))
#         mul_list = reduce(lambda x,y: x*y,list_of_self)
#         return mul_list
#     def get_sum(self):
#         x = str(self.value)
#         e = []
#         for i in x:
#             e.append(i)
#         spisok = e
#         int_ = list(map(lambda x:int(x),spisok))
#         selfvalue = reduce(lambda x,y:x+y,int_)
#         return selfvalue
#     def get_mul_table(self):
#         v = []
#         for i in range(1,11):
#             b = i*self.value
#             a = f'{self.value} X {i} = {b}'
#             v.append(a)
#             r = '\n'.join(v)
#         return r
# obj = Math(3)
# print(obj.get_factorial())
# print(obj.get_sum())
# print(obj.get_mul_table())

# task 9 - 2

# import math

# class Math:
#     def __init__(self, value):
#         self.value = value
    
#     def get_factorial(self):
#         fact = math.factorial(self.value)
#         return fact

#     def get_sum(self):
#         num_list = list(map(int, str(self.value)))
#         result = sum(num_list)
#         return result

#     def get_mul_table(self):
#         result = ('')
#         num_list = list(range(1, 11))
#         for num in num_list:
#             line = self.value * num
#             result += f'{self.value}x{num}={line}\n'
#         return result

# num = Math(11)

# print(num.get_factorial())
# print(num.get_sum())
# print(num.get_mul_table())

# task 10

# class ToDo:
#     instances = {}
#     def __init__(self, string) -> None:
#         self.string = string

#     def give_priority(self,priority):
#         self.instances.update({priority:self.string})

#     def list_of_tasks(self):
#         self.instances = sorted(self.instances.items(), key=lambda x: x[0]) 
#         return self.instances

# items1 = ToDo('сделать домашку')
# items2 = ToDo('сходить в кино')
# items3 = ToDo('выгулять собаку')
# items1.give_priority(1)
# items2.give_priority(3)
# items3.give_priority(2)
# print(ToDo.instances)
# print(items1.list_of_tasks())

# task 10 - 2

# class ToDo:
#     instances = {}
#     def __init__(self, delo):
#         self.delo = delo
#     def give_priority(self, priority):
#         ToDo.instances.update({priority: self.delo})
#     def list_of_tasks(self):
#         res = list(self.instances.items())
#         res.sort(key = lambda delo: delo[0])
#         return res
# todo1 = ToDo('Сходить в кино')
# todo2 = ToDo('Сделать домашку')
# todo3 = ToDo('Выгулять собаку')
# todo1.give_priority(3)
# todo2.give_priority(1)
# todo3.give_priority(2)
# print(ToDo.instances)
# print(todo1.list_of_tasks())

# task 2 - polimorfizm

# class Dog:
#     def voice(self):
#         print('Гав')
    
# class Cat:
#     def voice(self):
#         print('Мяу')
# def to_pet(dalban):
#     dalban.voice()
# barsik = Cat()
# rex = Dog()

# to_pet(barsik) 
# to_pet(rex) 

# task 3

# class Person:
#     def __init__(self,name,last_name):
#         self.name = name
#         self.last_name = last_name
#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}'
# class Employee(Person):
#     def __init__(self,name,last_name,work,status):
#         super().__init__(name,last_name)
#         self.work = work
#         self.status = status
#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}, я работаю в компании {self.work} на должности {self.status}'

# class Student(Person):
#     def __init__(self,name,last_name,university,course):
#         super().__init__(name,last_name)
#         self.university = university
#         self.course = course
#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}, я учусь в {self.university} на {self.course} курсе'

# def get_human_info(dalban):
#     print(dalban.get_info())
# person = Person('Азамат','Айталиев')
# employee = Employee('Азамат', 'Айталиев', 'The Most', 'официант')
# student = Student('Азамат', 'Айталиев', 'КГЮА', 1)
# get_human_info(employee) 
# get_human_info(student) 
# get_human_info(person) 

# task 4

# from abc import ABC, abstractmethod
# import math
# class Shape(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass
# class Triangle(Shape):
#     def __init__(self,base,height):
#         self.base = base
#         self.height = height
#     def get_area(self):
#         super().get_area()
#         return (0.5*self.base*self.height)
# class Square(Shape):
#     def __init__(self,length):
#         self.length = length
#     def get_area(self):
#         super().get_area()
#         return self.length**2
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
#     def get_area(self):
#         super().get_area()
#         return (self.radius**2)*math.pi
# triangle = Triangle(5,5)
# square = Square(5)
# circle = Circle(5)
# print(triangle.get_area()) 
# print(square.get_area()) 
# print(circle.get_area()) 

# task 5

# class OS:
#     def __init__(self,version):
#         self.version = version
    
# class Windows(OS):
#     def copy(self,text):
#         self.text = text
#         return f'скопирован текст "{self.text}" горячими клавишами CTRL + C'
# class MacOS(OS):
#     def copy(self,text):
#         self.text = text
#         return f'скопирован текст "{self.text}" горячими клавишами COMMAND + C'

# class Linux(OS):
#     def copy(self,text):
#         self.text = text
#         return f'скопирован текст "{self.text}" горячими клавишами CTRL + SHIFT + C'

# win  = Windows(2)
# mac = MacOS(3)
# lin = Linux(4)
# print(win.copy('Полиморфизм — одна из основных парадигм ООП'))
 
# print(mac.copy('Полиморфизм - разное поведение одного и того же метода в разных классах')) 
 
# print(lin.copy('На самом деле одинаковым является только имя метода, его исходный код зависит от класса'))

# task 6

# class Language:
#     def __init__(self,level,type):
#         self.level = level
#         self.type = type
# class Python(Language):
#     def write_function(self,func_name,arg):
#         self.func_name = func_name
#         self.arg = arg
#         return f'def {self.func_name}({self.arg}):'

#     def create_variable(self,var_name,value):
#         self.var_name = var_name
#         self.value = value
#         if type(value) == str:
#             return f"{self.var_name} = '{self.value}'"
#         else:
#             return f'{self.var_name} = {self.value}'
# class JavaScript(Language):
#     def write_function(self,func_name,arg):
#         self.func_name = func_name
#         self.arg = arg
#         return f'function {self.func_name}({self.arg}) ' + '{     };'
#     def create_variable(self,var_name,value):
#         self.var_name = var_name
#         self.value = value
#         if type(value) == str:
#             return f"let {self.var_name} = '{self.value}';"
#         else:
#             return f'let {self.var_name} = {self.value};'

# py = Python('high-level','interpreted')
# js = JavaScript('high-level','interpreted')
# print(py.write_function('get_code', 'a')) 
# print(py.create_variable('name', [1,2,3,4]))
# print(js.write_function('validate', 'form')) 
# print(js.create_variable('password', [1,2,3,4]))

# task 7

# class Money:
#     def __init__(self,country,symbol):
#         self.country = country
#         self.symbol = symbol
# class Dollar(Money):
#     rate = 84.80
#     def exchange(self,amount):
#         x = amount * self.rate
#         return f'$ {amount} равен {x} сомам'
# class Euro(Money):
#     rate = 98.40
#     def exchange(self,amount):
#         x = amount * self.rate
#         return f'€ {amount} равен {x} сомам'
# dol = Dollar('USA','$')
# eur = Euro('France','€')
# print(dol.exchange(100))
# print(eur.exchange(80))

# task 8 




# task 2 - mixins

# class RadioMixin:
#     def play_music(self,title):
#         print("Песня называется {title}")

# class Auto(RadioMixin):
#     def ride(self):
#         print("Riding on a ground")
    
# class Boat(RadioMixin):
#     def swim(self):
#         print("Floating on water")

# class Amphibian(Auto,Boat,RadioMixin):
#     pass


# auto = Auto()
# boat = Boat()
# obj = Amphibian()
# auto.play_music("title")
# boat.play_music("title")
# obj.play_music("title")

# task 3

# from datetime import datetime 

# class Clock:
#     def current_time(self):
#         print(datetime.now().strftime('%H:%M:%S'))

# class Alarm:
#     def on(self):
#         pass
#     def off(self):
#         pass
# class AlarmClock(Alarm,Clock):
#     def alarm_on(self):
#         print("Будильник включен")

# clock = AlarmClock()
# clock.current_time() 
# clock.alarm_on() 

# task 4

# from abc import ABC, abstractmethod

# class Coder(ABC):
#     count_code_time = 0
#     @abstractmethod
#     def get_info(self):
#         pass
#     @abstractmethod
#     def coding(self):
#         pass
    
# class Backend(Coder):
#     def __init__(self, experience, languages_backend):
#         self.experience = experience
#         self.languages_backend = languages_backend
#     def coding(self, val):
#         self.count_code_time += val
#     def get_info(self):
#         return f'{self.languages_backend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование'

# class Frontend(Coder):
#     def __init__(self, experience, languages_frontend):
#         self.experience = experience
#         self.languages_frontend = languages_frontend
#     def coding(self, val):
#         self.count_code_time += val
#     def get_info(self):
#         return f'{self.languages_frontend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование'
# class Fullstuck(Backend, Frontend):
#     pass
# a = Backend("Junior", "Python")
# b = Frontend("Middle", "Javascript")
# c = Fullstuck("Senior", "Python and JS")
# a.coding(12) 
# b.coding(45) 
# c.coding(17) 
# print(a.get_info()) 
# print(b.get_info()) 
# print(c.get_info()) 

# task 5

# class Square:
#     def __init__(self,side):
#         self.side = side
#     def get_area(self):
#         return self.side**2

# class Triangle:
#     def __init__(self, height, base):
#         self.height = height
#         self.base = base
#     def get_area(self):
#         return (0.5*self.base*self.height)
    
# class Pyramid(Triangle):
#     def __init__(self, height, base):
#         super().__init__(height, base)
#     def get_volume(self):
#         return int((1/3) * (self.base**2)*(self.height))
    
# pyramid = Pyramid(12, 11)
# print(pyramid.get_volume())