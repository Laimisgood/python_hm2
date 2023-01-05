# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

num = int(input("Введите число = "))
list_num = [i for i in range(-num, num+1)]

print(list_num)

file = open("file.txt","r")
x = file.readlines()
for i in range(len(x)):
    x[i] = int(x[i].strip())

print(x)

multiply = 1
for i in range(len(x)):
    multiply *= list_num[x[i]]

print(multiply)