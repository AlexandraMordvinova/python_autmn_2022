#todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы. 

#Пример:
#mass = [1,2,17,54,30,89,2,1,6,2]
#Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
#Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
#Для числа 17 нет минимального растояния т.к элемент в массиве один.

mass = [1, 3, 5, 7, 9, 5, 3, 1, 7, 1]
a=[int(1) for x in range(int(5))]
print(a.index(max(a))-a.index(min(a)))
#print("Для числа 1 минимальное расстояние в массиве по индексам: ", mas.index(1))
print('Для числа 9 нет минимального расстояния,т.к. элемент в массиве один')




