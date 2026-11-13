import gc

first = []
second = []

first.append(second)
second.append(first)

print("first ссылается на second:", first[0] is second)
print("second ссылается на first:", second[0] is first)

print("Сборщик включён?", gc.isenabled())

print("Пороги поколений:", gc.get_threshold())
print("Статистика поколений:")
for stat in gc.get_stats():
    print(stat)

f_id = id(first)
s_id = id(second)
del first
del second

collect = gc.collect()
print("gc.collect() вернул:", collect)
print("Статистика поколений после изменений:")
for stat in gc.get_stats():
    print(stat)

print("id после удаления ссылок:")
print(f_id)
print(s_id)
print()

gc.disable()
print("Сборщик включён?", gc.isenabled())
a = []
b = []
a.append(b)
b.append(a)

c = []
c.append(c)

f = []
g = []
h = []
f.append(g)
g.append(h)
h.append(f)
del a, b, c, f, g, h

col = gc.collect()
gc.enable()
print("gc.collect() собрал объектов:", col)
print("Статистика поколений после изменений:")
for stat in gc.get_stats():
    print(stat)
print()



print('Собрано до графа:')
for stat in gc.get_stats():
    print(stat)
node_a = {'name': 'A', 'edges': []}
node_b = {'name': 'B', 'edges': []}
node_c = {'name': 'C', 'edges': []}
node_d = {'name': 'D', 'independent': True}

node_a['edges'].append(node_b)
node_b['edges'].append(node_c)
node_c['edges'].append(node_a)


del node_a, node_b, node_c

print(f"Независимый узел D доступен: {node_d}")

collected_now = gc.collect()
print(f"Собрано объектов в этот раз: {collected_now}")
for stat in gc.get_stats():
    print(stat)