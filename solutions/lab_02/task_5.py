import sys, tracemalloc
a=[]
b=[1,2,3,4,5,6,7,8,9,10]
tuple =(1,2,3,4,5,6,7,8,9,10)
str = 'abcdefghij'
t=12345
n = None
print(a, 'Размер(в байтах):', sys.getsizeof(a))
print(b, 'Размер(в байтах):', sys.getsizeof(b))
print(tuple, 'Размер(в байтах):', sys.getsizeof(tuple))
print(str, 'Размер(в байтах):', sys.getsizeof(str))
print(t, 'Размер(в байтах):', sys.getsizeof(t))
print(n, 'Размер(в байтах):', sys.getsizeof(n))
print()

k = []
last = sys.getsizeof(k)
print(f"len={len(k)}  size={last}")

for i in range(100):
    k.append(i)
    s = sys.getsizeof(k)
    if s != last:
        print(f"len={len(k)}  size={s}  (+{s - last})")
        last = s

print()
tracemalloc.start()
numbers = list(range(100_000))

current, peak = tracemalloc.get_traced_memory()
print("Current memory: %.2f KiB" % (current / 1024))
print("Peak memory:    %.2f KiB" % (peak / 1024))
tracemalloc.stop()
print()

tracemalloc.start()
numbers1 = range(100_000)
current1, peak1 = tracemalloc.get_traced_memory()
print("Current memory: %.2f KiB" % (current1 / 1024))
print("Peak memory:    %.2f KiB" % (peak1 / 1024))
tracemalloc.stop()
