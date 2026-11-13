a = 10
b = a

print(a, b)
print(id(a), id(b))

a += 1

print(a, b)
print(id(a), id(b))

print()


first = [10, 20]
second = first

print(first, second)
print(id(first), id(second))

second.append(30)

print(first, second)
print(id(first), id(second))

second = [10,20,30]
print(f'first == second: {first==second}')
print(f'first is second: {first is second}')
second.append(40)
print(first, second)
print('id', id(first), id(second))
print()
#Практическое задание
conf1=['DevOps',  ["Alice", "Bob"], [["localhost", 8080], ["--debug", "--verbose"]]]
conf2 = conf1
print(conf1)
print(conf2)
conf2[2][1].append("--test")
print(conf1)
print(conf2)
conf3=['DevOps',  ["Alice", "Bob"], [["localhost", 8080], ["--debug", "--verbose"]]]
conf3[2][1].append("--production")
print(conf3)
print(conf1)
assert conf1 is not conf2
assert conf1[1] is not conf3[1]
assert conf1[2] is not conf3[2]
print("Конфигурации независимы")
