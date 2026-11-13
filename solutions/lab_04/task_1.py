values = [10, 20, 30]
iterator = iter(values)

print(iterator is values)
print(iter(iterator) is iterator)
print(next(iterator))
print(next(iterator))
print(next(iterator))

#print(next(iterator))


def consume(iterable) -> list:
    """Собирает элементы iterable, вручную используя iter() и next()."""
    a=[]
    iterator = iter(iterable)
    while True:
        try:
            a.append(next(iterator))
        except StopIteration:
            return a
# Список
print('list: ', consume([10, 20, 30]))
# Кортеж
print("tuple: ", consume((1, 2, 3)))
# Строка
print("string: ", consume("hello"))
# range
print("range: ", consume(range(5)))
# Частично использованный итератор
it = iter([100, 200, 300, 400])
next(it)  # пропустили 100
next(it)  # пропустили 200
print("iterator: ", consume(it))

lst = [1, 2, 3]

# Повторный обход списка - каждый раз создаётся НОВЫЙ итератор
print(consume(lst))   # [1, 2, 3]
print(consume(lst))   # [1, 2, 3]  снова всё с начала

# Повторный обход итератора - итератор ОДНОРАЗОВЫЙ
it = iter(lst)
print(consume(it))    # [1, 2, 3]
print(consume(it))    # []

def my_enumerate(iterable, start=0):
    a=[]
    it = iter(iterable)
    while True:
        try:
            a.append((start,next(it)))
            start += 1
        except StopIteration:
            return a

print(my_enumerate(['safs', 'faffa', 'faefaed'],5))
print(my_enumerate('aaababababa'))
print(my_enumerate(x ** 2 for x in range(5)))

def my_zip(first, second):
    first=iter(first)
    second = iter(second)
    a=[]
    while True:
        try:
            a.append((next(first), next(second)))
        except StopIteration:
            return a
print(my_zip(['safs', 'faffa', 'faefaed'], [3,56,567,4757,444]))
print(my_zip('moababababa', ['afafe','aeefef','cvxbcxb']))
print(my_zip((x ** 2 for x in range(5)), 'sjaekfjebdekf'))

