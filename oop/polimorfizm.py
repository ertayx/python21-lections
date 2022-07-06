"=======================Полиморфизм=========================="
# Полиморфизм - принцип ООП, в котором методы в разных классах называются одинаково. (один интерфейс - разный функционал) 


class Dog:
    def speak(self):
        print('gav gav')
class Cat:
    def speak(self):
        print('my my')
class Frog:
    def speak(self):
        print('kva kva')

animals = [Dog(), Cat(), Frog()]

for i in animals:
    i.speak()

print(dir(list))
print(dir(str))
print(dir(dict))

# __len__
'kjkj'== 4
[1,2,3[1,3,4]] == 4
{'a':1,'b':2} == 2


# __add__
'a'+'b'=='ab'
[1,2,3]+[4,5,6] == [1,2,3,4,5,6]
{'a':1}+{'b':2} == {'a':1,'b':2}
4+6 == 10