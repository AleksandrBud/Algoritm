import random


def my_sort(i_arr):
    for k in range(1, i_arr.__len__() - 1):
        for i in range(0, i_arr.__len__() - k):
            if i_arr[i] < i_arr[i + 1]:
                i_arr[i], i_arr[i + 1] = i_arr[i + 1], i_arr[i]
    return i_arr


main_arr = [random.randint(-100, 100) for _ in range(30)]
print(main_arr)
print()
print(my_sort(main_arr))
