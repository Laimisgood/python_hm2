# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}

num = int(input("Введите число = "))
dict_num = {}
sum_num = 0
for i in range(1,num+1):
    sum_num += round((1+1/i)**i,2)
    dict_num[i] = round((1+1/i)**i,2)
print(dict_num)
print(sum_num)