import random
import sys

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
ran_arr = [random.randint(-20, 20) for _ in range(0, 20)]
print(ran_arr)
for i in range(0, ran_arr.__len__() - 1):
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
print(sys.getsizeof(ran_arr))
print(sys.getsizeof(i))
print(sys.getsizeof(min_el))
print(sys.getsizeof(max_el))
print(sys.getsizeof(tmp_val))

#Можно сэкономить память убрав переменную tmp_val
for i in range(0, ran_arr.__len__() - 1):
    if i == 0:
        min_el = i
        max_el = i
    else:
        if ran_arr[i] > ran_arr[max_el]:
            max_el = i
        if ran_arr[i] < ran_arr[min_el]:
            min_el = i
ran_arr[max_el], ran_arr[min_el] = ran_arr[min_el], ran_arr[max_el]
print(ran_arr)
print()
print(sys.getsizeof(ran_arr))
print(sys.getsizeof(i))
print(sys.getsizeof(min_el))
print(sys.getsizeof(max_el))
