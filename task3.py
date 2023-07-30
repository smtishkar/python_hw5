# Создайте функцию генератор чисел Фибоначчи (см. Википедию)


# Подготовка --> без функции
# number = 10
# num1, num2 = 1,1
# num3 = 0
# print (num1, num2, sep="\n")
# for i in range (number+1):
#     num3 = num1 + num2
#     num1, num2 = num2, num3
#     print(num3)


# Рабочий вариант с yield
def fib(number: int) -> int:
    num1, num2 = 1, 1
    num3 = 0
    print(num1, num2, end=" ")
    for i in range(number+1):
        num3 = num1 + num2
        num1, num2 = num2, num3
        yield num3


print(*fib(10))


# Просто посмотрел, что будет если исспользовать print вместо yield
# def fib(number):
#     num1, num2 = 1,1
#     num3 = 0
#     print (num1, num2, sep="\n")
#     for i in range (number+1):
#         num3 = num1 + num2
#         num1, num2 = num2, num3
#         print(num3)

# print(*fib(10))
