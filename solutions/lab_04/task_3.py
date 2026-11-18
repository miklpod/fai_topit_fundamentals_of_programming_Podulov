from collections import deque
import tracemalloc


def read_measurements(lines):
    """Преобразует непустые строки в вещественные числа."""
    for line in lines:
        line = line.strip()
        if line:
            yield float(line)


def filter_range(values, minimum: float, maximum: float):
    """Пропускает только значения из закрытого диапазона."""
    for value in values:
        if value >= minimum and value <= maximum:
            yield value


def moving_average(values, window_size: int):
    """Выдает скользящее среднее для заданного размера окна."""
    if not isinstance(window_size, int) or isinstance(window_size,bool) or window_size <= 0:
        raise ValueError("window_size должен быть положительным")
    window = deque(maxlen=window_size)
    for value in values:
        window.append(float(value))
        if len(window) == window_size:
            yield sum(window) / window_size




raw_lines = ["10.0", "", "12.5", "100.0", "11.5", "13.0", "9.5"]
# a=list(read_measurements(raw_lines))
# print(list(read_measurements(raw_lines)))
# b=filter_range(a, 0.0, 50.0)
# print(list(filter_range(a, 0.0, 50.0)))
# print(list(moving_average(b, 2)))

print(list(moving_average(filter_range(read_measurements(raw_lines), 0.0, 50.0), 2)))

a=moving_average(filter_range(read_measurements(raw_lines), 0.0, 50.0), 2)
print(next(a))
print(next(a))
print(list(a))
#print(next(a)) StopIteration

new=moving_average(filter_range(read_measurements(raw_lines), 0.0, 50.0), 2)
print(list(new))


even_squares=[x**2 for x in range(1, 21) if x%2==0]
print(even_squares)

lengths = {len(s) for s in raw_lines if s}
print(lengths)

dict_squares={n:n**2 for n in range(1,11)}
print(dict_squares)

sum_gen = sum(x**2 for x in range(1, 100001))
print(sum_gen)

# Практическое расширение

def check(n):
    if not isinstance(n, int) or isinstance(n,bool) or n < 0:
        raise ValueError("n(или size) должен быть целым числом >= 0")

def take(n, iterable):
    check(n)
    it = iter(iterable)
    for _ in range(n):
        try:
            yield next(it)
        except StopIteration:
            return


def drop(n, iterable):
    check(n)
    it = iter(iterable)
    for _ in range(n):
        try:
            next(it)
        except StopIteration:
            return
    yield from it


def batch(iterable, size):
    check(size)
    current = []
    for item in iterable:
        current.append(item)
        if len(current) == size:
            yield current
            current = []
    if current:
        yield current

# take(n, it) делает ровно n обращений к next() и останавливается
p=moving_average(filter_range(read_measurements(raw_lines), 0.0, 50.0), 2)
print(list(take(2, p)))
# drop(n, it) пропускает n элементов через next(), затем делает yield из it
dr=moving_average(filter_range(read_measurements(raw_lines), 0.0, 50.0), 2)
print(list(drop(2, dr)))
# batch(it, size) копит не больше size элементов в буфере, при заполнении отдаёт tuple и очищает буфер. Остаток отдаётся последним пакетом
bat=moving_average(filter_range(read_measurements(raw_lines), 0.0, 50.0), 2)
print(list(batch(bat, 2)))



mem_test=(str(x**2) for x in range(100_000))

def gen():
    pipe = moving_average(filter_range(read_measurements(mem_test), 0, 100_000), 3)
    for _ in pipe:
        pass
def with_lists():
    a = [x**2 for x in range(100_000)]
    b = [float(s) for s in a]
    c = [x for x in b if 0 <= x < 100_000]
    d = [sum(c[i:i + 3]) / 3 for i in range(len(c) - 2)]


tracemalloc.start()
# get_traced_memory() возвращает (current, peak) в байтах
gen()
current, peak = tracemalloc.get_traced_memory()
print('Lazy generator:')
print("Current memory: %.1f KiB" % (current / 1024))
print("Peak memory: %.1f KiB" % (peak / 1024))
tracemalloc.stop()

tracemalloc.start()
with_lists()
current1, peak1 = tracemalloc.get_traced_memory()
print('With lists:')
print("Current memory: %.1f KiB" % (current1 / 1024))
print("Peak memory: %.1f KiB" % (peak1 / 1024))
tracemalloc.stop()