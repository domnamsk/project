def fact(n):
    temp = 1
    for i in range(1, n + 1):
        temp *= i
        yield temp


n = int(input("Укажите факториал какого числа Вы хотели бы узнать?\n"))
for _ in fact(n):
    print(_)