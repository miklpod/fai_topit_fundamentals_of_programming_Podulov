import copy

original = [
    ["Python", 5],
    ["Algorithms", 4],
]

alias = original
shallow = original.copy()
deep = copy.deepcopy(original)


original.append(["Databases", 5])
print(f'{original}, id(original)-{id(original)}, id(original[0])-{id(original[0])}, id(original[0][1])-{id(original[0][1])}')
print(f'{alias}, id(alias)-{id(alias)}, id(alias[0])-{id(alias[0])}, id(alias[0][1])-{id(alias[0][1])}')
print(f'{shallow}, id(shallow)-{id(shallow)}, id(shallow[0])-{id(shallow[0])}, id(shallow[0][1])-{id(shallow[0][1])}')
print(f'{deep}, id(deep)-{id(deep)}, id(deep[0])-{id(deep[0])}, id(deep[0][1])-{id(deep[0][1])}')
print()

original[0][1] = 3

print(f'{original}, id(original)-{id(original)}, id(original[0])-{id(original[0])}, id(original[0][1])-{id(original[0][1])}')
print(f'{alias}, id(alias)-{id(alias)}, id(alias[0])-{id(alias[0])}, id(alias[0][1])-{id(alias[0][1])}')
print(f'{shallow}, id(shallow)-{id(shallow)}, id(shallow[0])-{id(shallow[0])}, id(shallow[0][1])-{id(shallow[0][1])}')
print(f'{deep}, id(deep)-{id(deep)}, id(deep[0])-{id(deep[0])}, id(deep[0][1])-{id(deep[0][1])}')
print()

wrong_matrix = [[0] * 3] * 3
wrong_matrix[0][0] = 1
print(id(wrong_matrix[0]), id(wrong_matrix[1]), id(wrong_matrix[2]))
correct_matrix = [[0] * 3 for _ in range(3)]
correct_matrix[0][0] = 1
print(id(correct_matrix[0]), id(correct_matrix[1]), id(correct_matrix[2]))
print(wrong_matrix)
print(correct_matrix)
