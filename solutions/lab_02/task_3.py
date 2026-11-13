import sys

data = [1, 2, 3]
print("После создания:", sys.getrefcount(data))

alias = data
print("После создания alias:", sys.getrefcount(data))

container = [data]
print("После помещения в контейнер:", sys.getrefcount(data))

del alias
print("После del alias:", sys.getrefcount(data))

container.clear()
print("После очистки контейнера:", sys.getrefcount(data))


import weakref
class Record1:
    pass
record = Record1()
weak_record = weakref.ref(record)

print(weak_record())
del record
print(weak_record())
print()




#Практическое задание

class Record:
    pass
registry = weakref.WeakValueDictionary()

# Создаём три объекта Record
rec1 = Record()
rec2 = Record()
rec3 = Record()

# Регистрируем их в слабом словаре
registry["1"] = rec1
registry["2"] = rec2
registry["3"] = rec3
print([(key, value) for key, value in registry.items()])
# Удаляем сильную ссылку, остается слабая - удаляется сама
del rec3
print([(key, value) for key, value in registry.items()])
del rec2
print([(key, value) for key, value in registry.items()])