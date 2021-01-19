defef
exe_4(x, y):
return 1 / x ** abs(y)

def exe_4_use():
    print(exe_4(2, -2))


def exe_41(x, y):
    for i in range(abs(y - 1)):
        x *= x
    return 1 / x


def exe_41_use():
    print(exe_4(2, -2))