from time import time
# Функция - это полноправный объект
# Внутренняя функция может захватывать переменные из внешней функции


# def example(a):
#     def inner(b):
#         return a + b
#     return inner(1)
#
#
# print(example)


# def logger(f):
# #     def wrapper(*args):
# #         return f
# #     return wrapper()
# #
# #
# # print(logger(summ)(10, 3))


# def example(f):
#     def wrapper1():
#         return wrapper2()
#
#     def wrapper2():
#         return f
#     return wrapper1()
#
#
# print(example(summ)(2))


# def timer(f):
#     """
#     Декоратор, возвращающий результат функции summ(), со временем выполнения функции
#     """
#     def wrapper():
#         start = time()
#         return f
#
#     def wrapper2(start):
#         end = time()
#         return f"time: {''}"
#
#     return wrapper()
#
#
# @timer
# def summ(*args):
#     return sum(args)
#
#
# print(summ(2, 4))

