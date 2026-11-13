import sys
import tracemalloc

#задание 1
a=[]
b=[1,2,3,4,5,6,7,8,9,10]
tup =(1,2,3,4,5,6,7,8,9,10)
text = 'abcdefghij'
t=5
n = None
sizes = [
    {"scenario": "пустой список", "count": len(a), "size": sys.getsizeof(a)},
    {"scenario": "список из 10 чисел", "count": len(b), "size": sys.getsizeof(b)},
    {"scenario": "кортеж из 10 чисел", "count": len(tup), "size": sys.getsizeof(tup)},
    {"scenario": "строка из 10 символов", "count": len(text), "size": sys.getsizeof(text)},
    {"scenario": "целое число", "count": 1, "size": sys.getsizeof(t)},
    {"scenario": "None", "count": 1, "size": sys.getsizeof(n)},
]


#задание 2
k = []
last = sys.getsizeof(k)
growth=[{"length": len(k), "size": last, "diff": 0}]
for i in range(100):
    k.append(i)
    s = sys.getsizeof(k)
    if s != last:
        growth.append({"length": len(k), "size": s, "diff": s - last})
        last = s


#задание 3
traced=[]

tracemalloc.start()
numbers = list(range(100_000))
current, peak = tracemalloc.get_traced_memory()
traced.append({"scenario":'list(range(100_000))', "count":len(numbers), "size":sys.getsizeof(numbers), 'cur_b':current, 'peak_b':peak})
tracemalloc.stop()

tracemalloc.start()
numbers1 = range(100_000)
current1, peak1 = tracemalloc.get_traced_memory()
traced.append({"scenario":'range(100_000)', "count":len(numbers1), "size":sys.getsizeof(numbers1), 'cur_b':current1, 'peak_b':peak1})
tracemalloc.stop()

peak_ratio = traced[0]["peak_b"] / traced[1]["peak_b"]

# Вывод отчета

print("Часть 1. Размеры отдельных объектов")
for row in sizes:
    print(row["scenario"],'| элементов: ',  row["count"], '| размер в байтах: ', row["size"])

print()

print("Часть 2. Рост списка")
for row in growth:
    print('длина: ', row['length'], "| размер в байтах:", row['size'], '| разница с предыдущим:', row['diff'])

print()

print("Часть 3. Измерение через tracemalloc")

for row in traced:
    print(row['scenario'], '| элементов: ',  row["count"],'| размер в байтах: ', row["size"])
    print("Current memory: %.2f KiB" % (row["cur_b"]/1024))
    print("Peak memory:    %.2f KiB" % (row["peak_b"]/1024))
    print()
print("Отношение пиковых объемов (list / range): %.1f" % peak_ratio)