# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def div(*args):

    try:
        arg1 = int(input('Входные данные '))
        arg2 = int(input('Входной делитель '))
        res = arg1 / arg2
    except ValueError:
        return 'Ошибочное значение'
    except ZeroDivisionError:
        return 'Неправильный делитель! Нельзя делить на ноль'

    return res

    '''
    if arg2 != 0:
        return arg1 / arg2
    else:
        print('Ошибся номером! Делитель не может быть нулевым')
    '''


print(f'result  {div()}')