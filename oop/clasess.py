"================OOP==================="
# OOP - Object-oriented programming 
# ООП - обьектно-ориентированное программирование (парадигма)

class Person:
    name = "Настя"
    age = 12
    arms = 2
    legs = 2

    def walk(arg):
        print(arg)
        print("я иду")
    
    def add_age(self):
        self.age += 1

# person1 = Person()
# person1.add_age() # Новый вариант
# # Person.add_age(person1) # Старый вариант
# print(person1.age)

# Person.age = 17
# print(Person.age)

# person2 = Person()
# print(person2.age)


class Person:
    arms = 2
    legs = 2

    def init(self, name, age):
        """
        функция, которая вызывается, когда мы создаем обьект от класса
        self - ссылка на созданный обьект
        """
        self.name = name # мы добавляем в обьект self новый аттрибут name
        self.age = age # новый аттрибут age

    def add_age(self):
        """
        функция, которая принимает обьект и изменяет его возраст на 1
        """
        self.age += 1

    def str(self):
        """
        функция, которая вызывается, когда мы оборачиваем обьект в класс str или когда принтуем обьект
        функция str ничего кроме self не принимает и обязательно должна возвращать строку
        """
        return f"{self.name} - {self.age} y.o"

person1 = Person("Настя", 50)
print(person1)

person2 = Person("Жаркынай", 15)
print(person2)


'===============Аттрибуты класса================'
# атрибуты класса - пересенные внутри класса

'==================Методы класса============================='
# методы класса - функиция внутри класса

'===================Объекты класса==================='
# объект экземпляр instance класса - объект созданный по шаблону класса (он перенимает все аттрибуты и методы у класса)

'========================Аттрибуты и методы объекта============================'
# аттрибуты и методы которые есть у объекта но возможно их нет у класса
class A:
    var1 = 'переменная класса'

    def init(self):
        self.var2 = 'переменная объекта'

print(dir(A))
# ['class', 'delattr', 'dict', 'dir', 'doc', 'eq', 'format', 'ge', 'getattribute', 'gt', 'hash', 'init', 'init_subclass', 'le', 'lt', 'module', 'ne', 'new', 'reduce', 'reduce_ex', 'repr', 'setattr', 'sizeof', 'str', 'subclasshook', 'weakref', 'var1']


obj = A()
print(dir(obj))
# 'new', 'reduce', 'reduce_ex', 'repr', 'setattr', 'sizeof', 'str', 'subclasshook', 'weakref', 'var1']
# ['class', 'delattr', 'dict', 'dir', 'doc', 'eq', 'format', 'ge', 'getattribute', 'gt', 'hash', 'init', 'init_subclass', 'le', 'lt', 'module', 'ne', 'new', 'reduce', 'reduce_ex', 'repr', 'setattr', 'sizeof', 'str', 'subclasshook', 'weakref', 'var1', 'var2']
# print(A.var1)

print(obj.var1)
print(obj.var2)


'Класс имеет доступ только к атрибутам класса'
"Объект имеет доступ и к аттрибутам класса и к его аттрибутам"