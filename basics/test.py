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
string = input()
newString = (string[1:-1])
print(string[-1]+newString+string[0])



# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print(f'{i} FizzBuzz')
#     elif i % 5 == 0:
#         print (f'{i}Buzz')
#     elif i % 3  == 0:
#         print(f'{i}Fizz')
#     else:
#         print(i)