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
min_num = min(numbers)
max_num = max(numbers)
min_index = numbers.index(min_num)
max_index = numbers.index(max_num)

print("min_index =", min_index)
print("min_num =", min_num)
print("max_index =", max_index)
print("max_num =", max_num)

if min_index == max_index or abs(min_index - max_index) == 1:
    print("Немає цифр в цьому діапазоні!")
else:
        if min_index > max_index:
            min_index, max_index = max_index, min_index

        numbers_range_mult = 1

        for i in range(min_index + 1, max_index):
            numbers_range_mult *= numbers[i]

        print(f"Добуток дорівнює: {numbers_range_mult}")

# Суму елементів, що знаходяться між першим та останнім позитивними елементами
is_positive = False
first_index, last_index = 0, 0

for number in numbers:
    if number > 0:
        is_positive = True
if is_positive:
    for i in range(len(numbers)):
        if numbers[i] > 0:
            first_index = i
            break

    for j in range(len(numbers) - 1, -1, -1):
        if numbers[j] > 0:
            last_index = j
            break

    print("first_index =", first_index)
    print("last_index =", last_index)

    if first_index == last_index or abs(first_index - last_index) == 1:
        print("Немає цифр в цьому діапазоні!")
    else:
        if first_index > last_index:
            first_index, last_index = last_index, first_index

        numbers_range_sum = 0

        sum_el = sum(numbers[first_index+1:last_index])
        print("Сума елементів",sum_el)
else:
    print("Немає позитивних цифр в цьому діапазоні!")

# 2 Є список цілих, заповнений випадковими числами.
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
print(count_paired)
# ■ Створити список цілих, що містить лише непарні числа з першого списку;
count_unpaired = []
for i in numbers:
    if i % 2 != 0:
        count_unpaired.append(i)
print(count_unpaired)
# ■ Створити список цілих, що містить лише негативні числа з першого списку;
negative = []
for i in numbers:
    if i < 0:
        negative.append(i)
print(negative)
# ■ Створити список цілих, що містить лише позитивні числа з першого списку.
positive = []
for i in numbers:
    if i > 0:
        positive.append(i)
print(positive)

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





