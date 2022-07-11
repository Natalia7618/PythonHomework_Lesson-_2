# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции вводит пользователь через пробел.

import random
from unittest import result

list = []
n = 10
for i in range(n):
    list.append(random.randint(-n, n))
print('Список: ', list)

entered_positions = input("Введите две позиции от 0 до 9 через пробел: ")
pos1, pos2 = map(int, entered_positions.split(' '))
print("Введенные позиции: ", pos1, pos2)
print("Множители: ", list[pos1], list[pos2])

def multiplication (pos1, pos2):
    result = list[pos1] * list[pos2]
    return result

print ('Произведение =', multiplication(pos1, pos2))