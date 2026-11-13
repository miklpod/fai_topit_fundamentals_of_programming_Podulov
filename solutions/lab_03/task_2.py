measurements = [12, 15, 11, 18, 18, 9, 21, 15, 7, 18]

total = 0
min_val = float('inf')
max_val = float('-inf')
even = 0
n = 0

for x in measurements:
    total += x
    if x < min_val:
        min_val = x
    if x > max_val:
        max_val = x
    if x % 2 == 0:
        even += 1
    n += 1

mid = total / n
gt = 0
for x in measurements:
    if x > mid:
        gt += 1

print('сумма:', total)
print('минимум:', min_val)
print('максимум:', max_val)
print('четных чисел:', even)
print('больше среднего арифметического:', gt)

k=int(input())
flag=False
for x in range(len(measurements)):
    if measurements[x]==k:
        print(x)
        flag=True
        break
if not flag:
    print(-1)


import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

p=int(input())
print(is_prime(p))

import random
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def linear_search(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons


def binary_search(arr, target):
    comparisons = 0
    left, right = 0, len(arr) - 1

    while left <= right:
        comparisons += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, comparisons

sizes = [10, 100, 1000]
results = []
for size in sizes:
    arr = [random.randint(1, size * 10) for _ in range(size)]

    selection_sort(arr)

    # Выбираем элемент для поиска
    target = arr[random.randint(0, len(arr) - 1)]

    ind_lin, linear_comparisons = linear_search(arr, target)
    ind_bin, binary_comparisons = binary_search(arr, target)

    results.append({'size': size, 'linear_comparisons': linear_comparisons, 'binary_comparisons': binary_comparisons})
print(f"{'Размер'} {'Линейный'} {'Бинарный'}")
for r in results:
    print(f"{r['size']} {r['linear_comparisons']} {r['binary_comparisons']}")