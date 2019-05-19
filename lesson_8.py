import hashlib


def search_substring(i_str):
    len_str = int(len(i_str))
    o_arr = []
    for i in range(0, len_str):
        arr = [hashlib.sha1(i_str[i: n].encode('utf-8')).hexdigest() for n in range(i + 1, len_str + 1)]
        o_arr = o_arr + arr
    return o_arr


str = str(input('Введите строку: '))
for hash_value in search_substring(str):
    print(hash_value)
