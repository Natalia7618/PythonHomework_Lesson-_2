# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

n = float(input('Введите число: '))
str_n = str(n)
str_n = str_n.replace('.', '')
list_str = list(str_n)
list_num = map(int, list_str)
s = sum (list_num)
print(s)

