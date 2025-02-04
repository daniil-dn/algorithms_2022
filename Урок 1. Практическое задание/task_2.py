"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""


# Сложность первого алгоритма должна быть O(n^2) - квадратичная.

def first_min(lst_in: list) -> int:
    # O(n^2)
    for i in lst_in:  # O(n)
        is_min = True  # O(1)
        for j in lst_in:  # O(n)
            if i > j:  # O(1)
                is_min = False  # O(1)
        if is_min:  # O(1)
            return i  # O(1)


# Сложность второго алгоритма должна быть O(n) - линейная.
def second_min(lst_in: list) -> int:
    res_num = lst_in[0]  # O(1)
    for i in range(len(lst_in)):  # O(n)
        cur_num = lst_in[i]  # O(1)
        if cur_num < res_num:  # O(1)
            res_num = cur_num  # O(1)
    return res_num  # O(1)


print(first_min([2, 3, 5, 1, 4, 5, 10, 12, 0]))
print(second_min([2, 3, 5, 1, 4, 5, 10, 12, 0]))
