from dataclasses import dataclass

@dataclass(frozen=True) # делаем неизменяемым
class Submission:
    student_id: str
    laboratory_id: str
    attempt: int
    score: float
    comment: str = ""
    def __post_init__(self) -> None:
        if not self.student_id.strip():
            raise ValueError("student_id не должен быть пустым")
        if not self.laboratory_id.strip():
            raise ValueError("laboratory_id не должен быть пустым")
        if self.attempt <= 0:
            raise ValueError("attempt должен быть положительным числом")
        if not 0 <= self.score <= 100:
            raise ValueError("score должен быть в диапазоне от 0 до 100")
    def __eq__(self, other: Submission) -> bool:
        return (self.student_id == other.student_id
                and self.laboratory_id == other.laboratory_id
                and self.attempt == other.attempt
                and self.score == other.score
                and self.comment == other.comment)
class Student:
    def __init__(self, student_id: str, student_name: str) -> None:
        self.student_id = student_id
        self._submissions: list[Submission] = []
        self.student_name = student_name
    def add_submission(self, submission: Submission) -> None:
        if submission.student_id != self.student_id:
            raise ValueError(f"ID студента в работе ({submission.student_id}) не совпадает с ID текущего студента ({self.student_id}).")
        self._submissions.append(submission)
    @property
    def submissions(self):
        """Возвращает кортеж работ, защищая внутренний список от мутаций извне."""
        return tuple(self._submissions)

    @property
    def average_score(self):
        """Вычисляет средний балл по всем попыткам"""
        if not self._submissions:
            return 0.0
        return sum(sub.score for sub in self._submissions) / len(self._submissions)

    def best_score(self, laboratory_id: str):
        """Возвращает максимальный балл по конкретной лабораторной или None, если попыток не было"""
        scores = [sub.score for sub in self._submissions if sub.laboratory_id == laboratory_id]
        return max(scores) if scores else None

    @classmethod
    def from_full_name(cls, student_id: str, student_name: str) -> "Student":
        cleaned_name = " ".join(part.capitalize() for part in student_name.split())
        return cls(student_id=student_id.strip(), student_name=cleaned_name)

    @staticmethod
    def is_valid_id(identifier: str) -> bool:
        return (isinstance(identifier, str) and bool(identifier) and not any(ch.isspace() for ch in identifier))
    @property
    def sorted_submissions(self):
        return sorted(self._submissions, key=lambda x: (x.attempt, x.score))
    def __len__(self):
        return len(self._submissions)

    def __iter__(self):
        return iter(self._submissions)

    def __str__(self):
        return f"Студент: {self.student_name} (ID: {self.student_id}) - попыток: {len(self)}, средний балл: {self.average_score:.2f}"

    def __repr__(self):
        return f'Student(student_id: {self.student_id}, student_name: {self.student_name})'

student = Student("s101", "Иван Петров")
sub1 = Submission("s101", "lab_1", attempt=1, score=72.5, comment="Норм")
sub2 = Submission("s101", "lab_1", attempt=2, score=95.0, comment="+++")
sub3 = Submission("s101", "lab_2", attempt=1, score=88.0)
student.add_submission(sub1)
student.add_submission(sub2)
student.add_submission(sub3)

print(student)
print(repr(student))
print("Всего попыток:", len(student))
print("Лучший за lab_1:", student.best_score("lab_1"))

for item in student:
    print(f"{item.laboratory_id} (попытка {item.attempt}): {item.score}")

class Course:
    def __init__(self) -> None:
        self._students: dict[str, Student] = {}
    def add_student(self, student: Student):
        if student.student_id in self._students:
            raise ValueError(f"Студент с ID {student.student_id} уже зарегистрирован на курсе")
        self._students[student.student_id] = student
    def get_student(self, student_id: str):
        if student_id not in self._students:
            raise KeyError(f"Студент с ID {student_id} не найден на курсе")
        return self._students[student_id]
    def submit(self, submission: Submission):
        student = self.get_student(submission.student_id)
        student.add_submission(submission)

    def top_students(self, limit: int = 3):
        if limit < 0:
            raise ValueError("Параметр limit не может быть отрицательным")
        ranked = sorted(self._students.values(), key=lambda student: student.average_score,reverse=True)
        return ranked[:limit]
    def __len__(self):
        return len(self._students)
    def __iter__(self):
        return iter(self._students.values())
    def __contains__(self, student_id: str):
        return student_id in self._students

course = Course()
course.add_student(Student("s101", "Иван Петров"))
print('s101' in course)

student1 = Student.from_full_name(" s101 ", "  иван   ПЕТРОВ  ")
print(student1.student_id)  # 's101'
print(student1.student_name)  # 'Иван Петров'

print(student1)

print(Student.is_valid_id("s101"))   # True
print(Student.is_valid_id("s 101"))  # False


s1 = Submission("s101", "lab_1", attempt=2, score=90.0)
s2 = Submission("s101", "lab_1", attempt=1, score=75.0)
s3 = Submission("s101", "lab_2", attempt=1, score=95.0)
s1_copy = Submission("s101", "lab_1", attempt=2, score=90.0)

# Сравнение по содержимому
print(s1 == s1_copy)  # True
print(s1 == s2)       # False

# Сортировка без изменения исходного списка
student = Student("s101", "Иван Петров")
student.add_submission(s1)
student.add_submission(s2)
student.add_submission(s3)

# Отсортировано по (attempt, score): (1, 75.0), (1, 95.0), (2, 90.0)
print([(s.attempt, s.score) for s in student.sorted_submissions])

# Исходный порядок сохранён: (2, 90.0), (1, 75.0), (1, 95.0)
print([(s.attempt, s.score) for s in student.submissions])


# Приведите примеры работы стандартных функций `len()`, `iter()` и оператора `in` с созданными объектами.
course1 = Course()
s1 = Student("s101", "Иван Петров")
s2 = Student("s102", "Анна Смирнова")

course1.add_student(s1)
course1.add_student(s2)

course1.submit(Submission("s101", "lab_1", attempt=1, score=80.0))
course1.submit(Submission("s101", "lab_1", attempt=2, score=95.0))
course1.submit(Submission("s102", "lab_1", attempt=1, score=90.0))

# Функция len() вызывает __len__
print(len(course1))  # 2 (количество зарегистрированных студентов)
print(len(s1))      # 2 (количество попыток у студента s1)

# Функция iter() и цикл for вызывают __iter__
# Обход студентов на курсе
for student in course:
    print(student.student_name)

# Явное получение итератора по работам студента
sub_iterator = iter(s1)
print(next(sub_iterator))  # Submission(student_id='s101', laboratory_id='lab_1', attempt=1, score=80.0, comment='')
print(next(sub_iterator))  # Submission(student_id='s101', laboratory_id='lab_1', attempt=2, score=95.0, comment='')

# Оператор in вызывает __contains__
print("s101" in course)  # True
print("s999" in course)  # False

target = Submission("s101", "lab_1", attempt=2, score=95.0)
print(target in s1)      # True


print("Конец части 4")