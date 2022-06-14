x = int(input('Введите первое число: '))
z = int(input('Введите второе число: '))
y = input('Выберите операцию из следующих +-*/%**//: ')
if y == '+':
    print(x + z)
elif y == '-':
    print(x - z)
elif y == '*':
    print(x * z)
elif y == '**':
    print(x ** z)
elif y == '/':
    print(x / z)
elif y == '//':
    print(x // z)
elif y == '%':
    print(x % z)
else:
    print('Данной операции нет в системе')  