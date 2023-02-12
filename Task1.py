# ; Задача 22: Даны два неупорядоченных набора целых чисел 
# ; (может быть, с повторениями). 
# ; Выдать без повторений в порядке возрастания 
# ; все те числа, которые встречаются в обоих наборах.
# ; Пользователь вводит 2 числа. 
# ; n - кол-во элементов первого множества. 
# ; m - кол-во элементов второго множества.
# ;  Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12


n = int(input('Введите кол-во элементов первого множества:'))
my_set_n = set()
for i in range(n):
    my_set_n.add(input())
print('Множество:', my_set_n)

m = int(input('Введите кол-во элементов второго множества:'))
my_set_m = set()
for i in range(m):
    my_set_m.add(input())
print('Множество:', my_set_m)

set_joint = my_set_n.intersection(my_set_m)
list_join = list(map(int, set_joint))
list_join.sort()
print(list_join)