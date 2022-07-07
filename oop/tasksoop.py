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
#     def __init__(self,message):

class CustomError(Exception):
    def init(self, letters):
        self.letters = letters

    def check_letters(self, debil):
        self.debil = debil
        if self.debil.islower():
            raise Exception('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')
        else:
            return f'ВСЕ ОТЛЧНО! {debil}'

capitals_error = CustomError()
print(capitals_error.check_letters('as'))