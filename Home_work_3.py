import random
#1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
for i in range(2, 10):
    count_dig = 0
    for k in range(2, 100):
       if k % i == 0:
           count_dig = count_dig + 1
    print('Кратно {}, {} чисел'.format(i, count_dig))
print()

# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
# 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.
ran_arr = [random.randint(-20, 20) for _ in range(0, 20)]
print(ran_arr)
arr_index = []
for i in range(0, ran_arr.__len__()-1):
    if ran_arr[i] % 2 == 0:
        arr_index.append(i)
print(arr_index)
print()

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
for i in range(0, ran_arr.__len__()-1):
    if i == 0:
        min_el = i
        max_el = i
    else:
        if ran_arr[i] > ran_arr[max_el]:
            max_el = i
        if ran_arr[i] < ran_arr[min_el]:
            min_el = i
tmp_val = ran_arr[max_el]
ran_arr[max_el] = ran_arr[min_el]
ran_arr[min_el] = tmp_val
print(ran_arr)
print()

# 4. Определить, какое число в массиве встречается чаще всего.
max_count_el = 0
index_el = 0
for i in ran_arr:
    if ran_arr.count(i) > max_count_el:
        index_el = i
print('Чаще всего встречается число {}'.format(ran_arr[index_el]))
print()

# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
ran_arr = [random.randint(-20, 20) for _ in range(0, 20)]
min_el = 0
index_el = 0
for i in range(0, ran_arr.__len__() - 1):
    if ran_arr[i] < ran_arr[index_el] and ran_arr[i] < 0:
        index_el = i
print('Максимальный отрицательный элемени {}'.format(ran_arr[index_el]))
print()

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
for i in range(0, ran_arr.__len__()-1):
    if i == 0:
        min_el = i
        max_el = i
    else:
        if ran_arr[i] > ran_arr[max_el]:
            max_el = i
        if ran_arr[i] < ran_arr[min_el]:
            min_el = i
if min_el > max_el:
    tmp_el = min_el
    min_el = max_el
    max_el = tmp_val
sum_el = 0
for i in range(min_el + 1, max_el):
    sum_el = sum_el + ran_arr[i]
print('Сумма элементов м/д min и max {}'.format(sum_el))
print()

# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
min_el_1 = 0
min_el_2 = 0
for i in ran_arr:
    if i <= min_el_1:
        min_el_2 = min_el_1
        min_el_1 = i
    elif i < min_el_2:
        min_el_2 = i
print('Два наименьших елемента {}, {}'.format(min_el_1,min_el_2))
print()

# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.
arr_mine = []
for k in range(1, 5):
    arr_second = []
    summ_el = 0
    for i in range(1, 5):
        el = float(input('Введите элемент {} строки {}: '.format(i, k)))
        summ_el = summ_el + el
        arr_second.append(el)
    arr_second.append(summ_el)
    arr_mine.append(arr_second)
for i in arr_mine:
    str_tmp = ''
    for k in i:
        str_tmp = str_tmp + str(k) + ' '
    print(str_tmp)
print()

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
for i in range(0, arr_mine.__len__()):
    if i == 0:
        min_el_col = [el_row for el_row in arr_mine[i]]
    else:
        row = arr_mine[i]
        for z in range(0, row.__len__()):
            if row[z] < min_el_col[z]:
                min_el_col[z] = row[z]
max_el = 0
for i in min_el_col:
    if max_el < i:
        max_el = i
print('Максимальный элемент среди минимальных элементов столбцов {}'.format(max_el))