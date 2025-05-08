inp = input('Введите числа через запятую: ')

inp_str = inp.split(',')
numbers = []
for num_str in inp_str:
    numbers.append(int(num_str.strip()))


even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(f'Четные числа: {even_numbers}')


max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(f'Максимальное число: {max_num}')

min_num = numbers[0]
for num in numbers:
    if num < min_num:
        min_num = num
print(f'Минимальное число: {min_num}')

n = len(numbers)
for i in range(n):
    for j in range(0, n-i-1):
        if numbers[j] > numbers[j+1]:
            temp = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = temp

print(f'Отсортированный список: {numbers}')