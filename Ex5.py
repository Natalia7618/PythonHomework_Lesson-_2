# Реализуйте алгоритм перемешивания списка.

import random

list = []
n = 10
for i in range(n):
    list.append(random.randint(11,19))
print('Изначальный список: ', list)
random.shuffle(list)
print ('Перемешанный список: ', list)