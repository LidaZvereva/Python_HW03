# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

num = int(input('Введите размер списка '))
list = []

for i in range(num):
    list.append(randint(0, 9))
print(list)

print(sum(list[1::2]))