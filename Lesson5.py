#1 У списку цілих, заповненому випадковими числами
import random
Num_size = 10
numbers = []
for i in range(Num_size):
    numbers.append(random.randint(-10,10))
print(numbers)

# обчислити:

# Сума негативних чисел
count_neg_sum = 0
for i in numbers:
    if i < 0:
        count_neg_sum += i
print(count_neg_sum)

# Сума парних чисел
count_paired_sum = 0
for i in numbers:
    if i % 2 == 0:
        count_paired_sum += i
print(count_paired_sum)

# Сума непарних чисел
count_unpaired_sum = 0
for i in numbers:
    if i % 2 != 0:
        count_unpaired_sum += i
print(count_unpaired_sum)

# Добуток елементів з індексами кратними 3
multi = 1
for i in range(len(numbers)):
    if i % 3 == 0 and i != 0:
        multi *= numbers[i]
print(multi)

# Добуток елементів між мінімальним та максимальним елементом
multi_min_max = min(numbers)*max(numbers)
print(multi_min_max)

# # Суму елементів, що знаходяться між першим та останнім позитивними елементами
# for i in numbers:
#     if i > 0:
#         index1 = numbers.index(i)
#         print(i)
#         print(index1)
#         break
# for j in numbers[::-1]:
#     if j > 0:
#         index2 = numbers.index(j)
#         print(j)
#         print(index2)
#         break
# sum_el = sum(numbers[index1+1:index2])
# print(sum_el)

# index1 = -1
# i=0
# while index1 < 0 and i <= Num_size:
#     if numbers.index(i) > 0:
#         index1 = numbers.index(i)
#     else:
#         i += 1

#2 Є список цілих, заповнений випадковими числами.
import random
Num_size = 10
numbers = []
for i in range(Num_size):
    numbers.append(random.randint(-10,10))
print(numbers)

# На підставі даних цього масиву потрібно:

# Створити список цілих, що містить лише парні числа з першого списку;
count_paired = []
for i in numbers:
    if i % 2 == 0:
        count_paired.append(i)
print(count_paired )

# ■ Створити список цілих, що містить лише непарні числа з першого списку;
count_unpaired = []
for i in numbers:
    if i % 2 != 0:
        count_unpaired.append(i)
print(count_unpaired )

# # ■ Створити список цілих, що містить лише негативні числа з першого списку;

# negative = []
# for i in numbers:
#     if i < 0

# ■ Створити список цілих, що містить лише позитивні числа з першого списку.



# Додаткові завдання по матрицях (надіслати як завжди мені в лс після виконання
# основного дз):
# -створити матрицю 10 на 10, заповнити рандомними значеннями від 10 до 99
# -вивести на екран
# - вивести суму чисел головної діагоналі матриці
# - вивести мінімальне та максимальне значення побічної діагоналі матриці
# - ввести з клавіатури порядковий номер стовпця - вивести цифри з цього
#  стовпця на екран (аналогічно зробити з рядком)
# - ввести з клавіатури порядковий номер одного стовпця і потім іншого стовпця
# і поміняти їх місцями в матрицю (аналогічно зробити з рядком)





