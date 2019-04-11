# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
import random

print('ЗАДАЧА 1')
count = int(input('Введите количество элементов списка: '))
mylist = []
n = 0
while n < count:
    mylist.append(random.randint(0, 100))
    n +=1
print(mylist)
print('Квадраты чисел:')
for i in range(count):
    sort_list = mylist[i]**2
    print(sort_list) #нужно попробовать вывести значения в строку


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

print('ЗАДАЧА 2')
print('Даны два списка:')
fruit1 = ['Киви', 'Яблоко', 'Слива', 'Груша', 'Клубника']
fruit2 = ['Яблоко', 'Маракуйя', 'Клубника','Персик', 'Абрикос', 'Киви']
print(fruit1)
print(fruit2)
print('Список фруктов, присутствующих в обоих списках:')
result = list(set(fruit1) & set(fruit2))
print(result)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

print('ЗАДАЧА 3')
count = int(input('Введите количество элементов списка: '))
mylist = []
n = 0
while n < count:
    mylist.append(random.randint(0, 100))
    n +=1
print('Список, заполненный произвольными числами:', mylist)
mylist1 = [0]*count
mylist2 = [0]*count
mylist3 = [0]*count
for i in range(count):
    if mylist[i] % 3 == 0:
        mylist1[i] = mylist[i]
        print('Элементы, кратные трем: ', mylist[i])
for i in range(count):
    if mylist[i] % 4 != 0:
        mylist2[i] = mylist[i]
        print("Элемент, не кратный четырем: ", mylist2[i])
for i in range(count):
    if mylist[i] > 0:
        mylist3[i] = mylist[i]
        print('Элемент положительный', mylist3[i])





