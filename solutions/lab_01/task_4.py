student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10
#1
print(student[0], student[-1])
#2
name = student[0:4]
surname = student[5::]
print(name)
print(surname)

#3
print(student.lower())
print(student.upper())

#4
print(f'{student[0]}.{student[5]}.')

#5
print(course[::-1])

#6
percent = completed / total * 100

# Способ 1: оператор %
result1 = "%s — %s: %d/%d (%.1f%%)" % (student, course, completed, total, percent)
print(result1)

# Способ 2: метод .format()
result2 = "{} — {}: {}/{} ({:.1f}%)".format(student, course, completed, total, percent)
print(result2)

# Способ 3: f-строка
result3 = f"{student} — {course}: {completed}/{total} ({percent:.1f}%)"
print(result3)

#7
symbol = "Я"

print(symbol)
print(ord(symbol))
print(chr(ord(symbol)))
print(symbol.encode("utf-8"))
print(len(symbol.encode("utf-8")))

#8
#symbol[0]="А"