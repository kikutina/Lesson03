#Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль
def function(var_1, var_2):
        return  var_1 / var_2
        #try:
           # if var_2 == 0:
        #except ZeroDivisionError:
                #print('Ошибка! На ноль делить нельзя!')

a = float(input('Введите первое значение: '))
b = float(input('Введите второе значение: '))
if b !=0:
    print(function(a,b))
else:
    print('Ошибка! На ноль делить нельзя!')