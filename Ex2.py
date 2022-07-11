# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def multiplication(n):
    return 1 if n == 0 else n * multiplication(n - 1)

n = int(input('Введите число: '))
i = 1
while i <= n:
    print (multiplication(i))
    i += 1

