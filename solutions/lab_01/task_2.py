'''
1)b=a поэтому a==b должно выдать True
2)b=a т.е. они указывают на один и тот же объект, поэтому a is b True
3)a==c True, потому что 1000==1000(и там, и там тип int)
4)a is c False, потому что это разные объекты в памяти
'''

a = 1000
b = a
c=int('1000')
#c = None


print("Типы:", type(a), type(b), type(c))
print("Идентификаторы:", id(a), id(b), id(c))
print("a == b:", a == b)
print("a is b:", a is b)
print("a == c:", a == c)
print("a is c:", a is c)

#print("c is None:", c is None)

first = "python"
second = "py" + "thon"

print(first == second)
print(first is second)
'''
first==second=='python'
first и second создают один и тот же объект, поэтому first is second True
CPython вычисляет строковые литералы еще во время компиляции
'''