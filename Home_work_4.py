# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random
import timeit
import cProfile


def var_1():
    ran_arr = [random.randint(-20, 20) for _ in range(0, 20)]
    index_el = 0
    for i in range(0, ran_arr.__len__() - 1):
        if ran_arr[i] < ran_arr[index_el] and ran_arr[i] < 0:
            index_el = i
#    print('Максимальный отрицательный элемени {}'.format(ran_arr[index_el]))


def var_2():
    min_el = 0
    for i in [random.randint(-20, 20) for _ in range(20)]:
        if i < min_el and i < 0:
            min_el = i
#    print('Максимальный отрицательный элемени {}'.format(min_el))


def var_3():
    min_el = min([i for i in [random.randint(-20, 20) for _ in range(20)]])
#    print('Максимальный отрицательный элемени {}'.format(min_el))


def v_4():
    print(timeit.timeit("var_1()", setup="from __main__ import var_1", number=200000))


# var_1()
# var_2()
# var_3()

cProfile.run('v_4()')
print(timeit.timeit("var_1()", setup="from __main__ import var_1", number=200000))
print(timeit.timeit("var_2()", setup="from __main__ import var_2", number=200000))
print(timeit.timeit("var_3()", setup="from __main__ import var_3", number=200000))
