# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
#  5, 5, 4, 2, 3, 4, 5 -> 2, 2, 4, 2, 3, 4, 2
# marks_list = [int(input()) for _ in range(int(input('Введите кол-во оценок: ')))]
# maxx = marks_list[0]
# minn = marks_list[0]
# for el in marks_list:
#     if el < minn:
#         minn = el
#     if el > maxx:
#         maxx = el
# for ind in range(0, len(marks_list)):
#     if marks_list[ind] == maxx:
#         marks_list[ind] = minn
# print(marks_list)

# 1. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# *Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)*

def simple_number(number):
     for i in range(2, number // 2 + 1):
         if number % i == 0:
             return 'Число не простое'
     return 'Число простое'
print (simple_number())


