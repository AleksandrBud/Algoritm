# 1. Пользователь вводит данные о количестве предприятий, их наименования
# и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего
# и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
# Примечание: для решения задач попробуйте применить какую-нибудь коллекцию
# из модуля collections.

import collections


def ins_kv(num_kv):
    return(float(input('Введите прибыль за {} квартал: '.format(num_kv))))


def ins_name():
    name = input('Введите название предприятия: ')
    kvs = [ins_kv(i + 1) for i in range(4)]
    sum_kvs = (kvs[0] + kvs[1] + kvs[2] + kvs[3]) / 4
    man_tmp = Manufacture(name, kvs[0], kvs[1], kvs[2], kvs[3], sum_kvs)
    return(man_tmp)


def print_reult(i_man):
    sum_arr = [i.year for i in i_man]
    sr_znach = sum(sum_arr) / sum_arr.__len__()
    for i in i_man:
        print('Прибыль меньше средней у:')
        if i.year < sr_znach:
            print(i.name)
    for i in i_man:
        print('Прибыль больше средней у:')
        if i.year >= sr_znach:
            print(i.name)


col_man = int(input('Введите количество предприятий: '))
Manufacture = collections.namedtuple('Manufacture', ['name', 'kv_1', 'kv_2', 'kv_3', 'kv_4', 'year'])
manufactures = [ins_name() for _ in range(col_man)]
print_reult(manufactures)
