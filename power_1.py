#4. Программа принимает действительное положительное число n и целое отрицательное число p.
# Необходимо выполнить возведение числа n в степень p. Задание необходимо реализовать в виде функции mp_func(n, p).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
#
#На самом деле, странная задача. Зачем было по условию делать степень отрицательной, лично мне не очень понятно, принципы всё
#равно одни и те же.
#
#   Способ 1:

def pow(n:float, p:int):
    if p >= 0: return 'Неверный показатель степени'
    res = 1
    for c in range(abs(p)):
        res *= n
    return 1/res

print(pow(3.0, -4))
print(pow(3.0, 4))