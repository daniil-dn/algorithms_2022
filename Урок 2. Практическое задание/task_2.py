"""
Задание 2.	Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""


def even_odd_finding_cycle(num):
    is_find = True
    res_even = 0
    res_odd = 0

    while is_find:

        to_check = num % 10
        num = num // 10

        if to_check % 2 == 0:
            res_even += 1
        else:
            res_odd += 1
        if num == 0:
            return res_even, res_odd


def even_odd_finding(num, res=[0, 0]):
    if num == 0:
        return tuple(res)
    to_check = num % 10
    num = num // 10
    if to_check % 2 == 0:
        res[0] += 1
    else:
        res[1] += 1

    return even_odd_finding(num, res)


if __name__ == "__main__":
    num = input('Enter the number:\n')
    print(f"Количество четных и нечетных цифр в числе равно: {even_odd_finding_cycle(int(num))}")
    print(f"Количество четных и нечетных цифр в числе равно: {even_odd_finding(int(num))}")
