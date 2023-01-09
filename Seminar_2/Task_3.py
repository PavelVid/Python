# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}

n = int(input('Введите число N: '))


def sequence(n):
    return [round((1 + 1 / x) ** x, 2) for x in range(1, n + 1)]
print(sequence(n))
print(round(sum(sequence(n))))
