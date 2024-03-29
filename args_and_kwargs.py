#a, *b, c, d = '123456789'
# def example(a, b, c, *, d):  * здесь означает, что все аргументы справа после этой звёздочки ОБЯЗАТЕЛЬНО должны быть именоваными,
# то есть если при вызове этой функции example(), последним аргументом передать не именованый аргумент, допустим d=4, а просто 4, то вылетит ошибка, это надо запомнить.
#
#
# example(1, 2, 3, 4)
# Правила:
# / - все что слева - это не именованные аргументы(args)
# * - все что справа - это именованные аргументы - keyword args(kwargs)
# *args - собирает все неименованные аргументы в кортеж
# **kwargs - собирает все именованные аргументы в словарь, в котором ключ - это именованный аргумент,
# а значение - это и есть значение аргумента

def print_args(*args):
    print(*args, sep='\n')


# print_args(1, 2, 3, 4, 5)


def print_kwargs(**kwargs):
    print(kwargs)
# print_kwargs(one=1, two=2, three=3)










# a, b, c = '123'
# print(a, b, c)  интерпретатор понимает, что количество переменный равно количеству элементов строки,
# поэтому он выведет 1 2 3
# =========================
# a, b, c = '12'
# print(a, b, c)  интерпретатор выведет ошибку, потому что количествов эелементов строки меньше, чем самих переменных
# =========================
# Распаковки
# Распаковки обозначаются символом *, который итерирует объект и возвращает все значения
# Пример:
# a, *b, c = '12345'
# print(a, b, c)  1 ['2', '3', '4'] 5
# Как размышлял интерпретатор, чтобы выполнить этот код. Для начала он присвоил переменной a значение первого элемента строки, затем он дошел до переменной b, перед которой стоял значок "*", и интерпретатор понял,
# что все последующие значения будут итерируемыми, или рампакованными и присоенными переменной b, но после переменной b стоит переменная c, перед которой ничего нет, а значит она принимает в себя только одно значение: последнее,
# а значит что переменная b не может до конца принимать в себя все значения элементов строки, поэтому последнее значение будет присвоено переменной c, а предпоследнее - переменной b



