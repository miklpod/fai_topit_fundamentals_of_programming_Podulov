submissions = [
    ("anna", "lab_01", 5),
    ("boris", "lab_01", 4),
    ("anna", "lab_02", 5),
    ("daria", "lab_01", 3),
    ("boris", "lab_02", 5),
    ("anna", "lab_01", 4),

]
# 1) Множество всех студентов (уникальные имена)
students = {s[0] for s in submissions}

# 2) Множество всех сданных лабораторных работ (уникальные идентификаторы)
labs = {s[1] for s in submissions}

# 3) Словарь: студент -> список его попыток
attempts_by_student = {}
for s in submissions:
    if s[0] not in attempts_by_student:
        attempts_by_student[s[0]] = []
    attempts_by_student[s[0]].append(s)

# 4) Словарь: (студент, лабораторная) -> лучший балл
best_scores = {}
for s in submissions:
    key = (s[0], s[1])
    best_scores[key] = max(best_scores.get(key, -1), s[2])

# 5) Словарь: (студент, лабораторная) -> количество попыток
attempt_counts = {}
for s in submissions:
    key = (s[0], s[1])
    attempt_counts[key] = attempt_counts.get(key, 0) + 1

# Словарь "лабораторная -> множество студентов, её сдававших"
# нужен для поиска студентов, сдавших обе работы.
students_per_lab = {}
for s in submissions:
    students_per_lab.setdefault(s[1], set()).add(s[0])

# Сдали обе работы:
common_students = set.intersection(*students_per_lab.values())
print(common_students)

new_record = ("daria", "lab_02", 4)

students.add(new_record[0])                       # set: O(1)
labs.add(new_record[1])                           # set: O(1)
attempts_by_student.setdefault(new_record[0], []).append(new_record)  # dict+list: O(1)

key = (new_record[0], new_record[1])
best_scores[key] = max(best_scores.get(key, -1), new_record[2])       # dict: O(1)
attempt_counts[key] = attempt_counts.get(key, 0) + 1                  # dict: O(1)
students_per_lab.setdefault(new_record[1], set()).add(new_record[0])  # dict+set: O(1)
print(students_per_lab)
inf=list(input().split())

match inf[0]:
    case 'student':
        if len(inf)==2 and inf[1] in attempts_by_student:
            print(f'Все попытки студента {inf[1]}')
            for _,x,y in attempts_by_student[inf[1]]:
                print(x,y)
        else:
            print("Некорректный ввод аргументов")
    case 'best':
        if len(inf)==3 and (inf[1], inf[2]) in best_scores:
            print(f'Лучшая попытка студента {inf[1]} по лабораторной {inf[2]}')
            print(best_scores[(inf[1], inf[2])])
        else:
            print("Некорректный ввод аргументов")
    case 'attempts':
        if len(inf)==3 and (inf[1], inf[2]) in attempt_counts:
            print(f'Все попытки студента {inf[1]} по лабораторной {inf[2]}')
            print(attempt_counts[(inf[1], inf[2])])
        else:
            print("Некорректный ввод аргументов")
    case 'completed':
        if len(inf)==2 and inf[1] in students_per_lab:
            print(f'Все студенты, кто сдал лабораторную {inf[1]}')
            print(students_per_lab[inf[1]])
        else:
            print("Некорректный ввод аргументов")
    case _:
        print("Некорректная команда")