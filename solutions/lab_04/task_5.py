from abc import ABC, abstractmethod
from datetime import datetime, date
from task_4 import Student, Submission

class CourseEvent(ABC):
    """Общая информация о событиях курса"""
    @property
    @abstractmethod
    def created_at(self) -> datetime:
        """Время создания события (только для чтения)"""
        pass

    @property
    @abstractmethod
    def student_id(self) -> str:
        """Идентификатор студента, к которому относится событие"""
        pass

    @abstractmethod
    def describe(self) -> str:
        """Человекочитаемое описание события"""
        pass


class SubmissionEvent(CourseEvent):
    """Сдача работы"""
    def __init__(self, submission: Submission):
        super().__init__()
        self.submission = submission
        self._created_at = datetime.now()

    @property
    def student_id(self) -> str:
        return self.submission.student_id
    @property
    def created_at(self) -> datetime:
        return self._created_at

    def describe(self):
        return f'Сдача. Студент {self.student_id} сдал {self.submission.laboratory_id}, попытка {self.submission.attempt}. Дата: {self.created_at}'

class AttendanceEvent(CourseEvent):
    """Посещение"""
    def __init__(self, student_id, att_date):
        super().__init__()
        self.att_date = att_date
        self._student_id = student_id
        self._created_at = datetime.now()

    @property
    def student_id(self):
        return self._student_id

    @property
    def created_at(self):
        return self._created_at

    def describe(self):
        return f"Посещение. id студента: {self.student_id}. Создан: {self.created_at}. Дата посещения: {self.att_date}"

class CommentEvent(CourseEvent):
    """Событие с комментарием"""
    def __init__(self,student_id, comment):
        super().__init__()
        self.comment = comment
        self._student_id = student_id
        self._created_at = datetime.now()
    @property
    def student_id(self):
        return self._student_id
    @property
    def created_at(self):
        return self._created_at

    def describe(self):
        return f"Комментарий: {self.comment}. id студента: {self.student_id}. Создан: {self.created_at}"

class CourseJournal:
    """Журнал событий"""
    def __init__(self):
        self._events: list[CourseEvent] = []

    def __len__(self):
        return len(self._events)

    def __iter__(self):
        return iter(self._events)

    def __getitem__(self, item):
        return self._events[item]

    def add_event(self, event: CourseEvent):
        self._events.append(event)

    def events_for_student(self, student_id):
        """Генератор событий для конкретного студента."""
        for event in self._events:
            if event.student_id == student_id:
                yield event
    def events_by_type(self, event_type):
        """Генератор событий определённого типа"""
        for event in self._events:
            if isinstance(event, event_type):
                yield event

    def __str__(self):
        return f"Журнал курса ({len(self)} событий)"

    def __repr__(self):
        return f"CourseJournal(events={len(self)})"

    def summary(self):
        """Возвращает сводку без раскрытия внутреннего списка"""
        by_type={}
        by_student={}
        for event in self._events:
            type_name=type(event).__name__
            by_type[type_name]=by_type.get(type_name,0)+1
            by_student[type_name]=by_student.get(type_name,0)+1
        return {
            "by_type": by_type,
            "by_student": by_student,
            "total_events": len(self._events),
            "unique_students": len(by_student),
        }

def render_timeline(events) -> str:
    """Формирует временную шкалу, вызывая describe() у каждого события."""
    res=[]
    for event in sorted(events, key=lambda event: event.created_at):
        res.append(event.describe())
    return "\n".join(res)


class ScoreView:
    """Ленивое представление результатов только для событий сдачи."""
    def __init__(self, events) -> None:
        self._events = events

    def __iter__(self):
        for event in self._events:
            if isinstance(event, SubmissionEvent):
                yield event.submission.score

# Практическое расширение
class DeadlineEvent(CourseEvent):
    """Событие с информацией о сроке сдачи работы."""
    def __init__(self, student_id: str, laboratory_id: str, deadline: date) -> None:
        self._student_id = student_id
        self.laboratory_id = laboratory_id
        self.deadline = deadline
        self._created_at = datetime.now()

    @property
    def student_id(self) -> str:
        return self._student_id

    @property
    def created_at(self) -> datetime:
        return self._created_at

    def describe(self) -> str:
        return f"Дедлайн. Студент {self.student_id}, работа {self.laboratory_id}. Срок сдачи: {self.deadline}"
class FilteredJournalView:
    """Ленивое фильтруемое представление журнала событий."""

    def __init__(self, journal, predicate) -> None:
        self._journal = journal
        self._predicate = predicate

    def __iter__(self):
        for event in self._journal:
            if self._predicate(event):
                yield event

if __name__ == "__main__":
    # 1. Создаём 3 студентов
    s1 = Student("s101", "Иван Петров")
    s2 = Student("s102", "Анна Смирнова")
    s3 = Student("s103", "Дмитрий Соколов")

    # 2. Создаём журнал и добавляем 10 событий разных типов (включая 2 попытки сдачи одной работы lab_1 от студента s101)
    journal = CourseJournal()

    journal.add_event(AttendanceEvent(s1.student_id, date(2026, 5, 1)))
    journal.add_event(AttendanceEvent(s2.student_id, date(2026, 5, 1)))
    journal.add_event(AttendanceEvent(s3.student_id, date(2026, 5, 1)))

    journal.add_event(SubmissionEvent(Submission(s1.student_id, "lab_1", attempt=1, score=65.0)))
    journal.add_event(CommentEvent(s1.student_id, "Нужно доработать проверку инвариантов"))
    journal.add_event(SubmissionEvent(Submission(s1.student_id, "lab_1", attempt=2, score=95.0)))

    journal.add_event(SubmissionEvent(Submission(s2.student_id, "lab_1", attempt=1, score=88.5)))
    journal.add_event(CommentEvent(s2.student_id, "Чистый код, отличная работа!"))

    journal.add_event(SubmissionEvent(Submission(s3.student_id, "lab_1", attempt=1, score=74.0)))
    journal.add_event(CommentEvent(s3.student_id, "Добавьте тесты для граничных случаев"))

    # 3. Выборка событий одного студента (генератор)
    print("=== События студента s103 ===")
    for event in journal.events_for_student("s103"):
        print(" ", event.describe())

    # 4. Выборка событий одного типа (генератор)
    print("\n=== Все комментарии ===")
    for event in journal.events_by_type(CommentEvent):
        print(" ", event.describe())

    # 5. Срез журнала
    print("\n=== Срез журнала [3:6] ===")
    for event in journal[3:6]:
        print(" ", event.describe())

    # 6. Временная шкала (полиморфная обработка)
    print("\n=== Временная шкала всего курса ===")
    print(render_timeline(journal))

    # 7. Расчёт статистики по ScoreView (с проверкой повторного обхода)
    scores = ScoreView(journal)

    # Первый проход
    count = sum(1 for _ in scores)
    # Второй проход
    total = sum(scores)
    # Третий и четвёртый проходы
    min_score = min(scores)
    max_score = max(scores)
    avg_score = total / count if count else 0.0

    print("\n=== Статистика по ScoreView ===")
    print(f"Всего сдач: {count}")
    print(f"Мин: {min_score}, Макс: {max_score}, Средний: {avg_score:.2f}")
    print(f"Повторный обход (список): {list(scores)}")
    print()
    # Практическое расширение
    # Добавляем события дедлайнов в существующий журнал
    journal.add_event(DeadlineEvent("s101", "lab_5", date(2026, 5, 20)))
    journal.add_event(DeadlineEvent("s102", "lab_5", date(2026, 5, 20)))

    # 1. Полиморфизм: render_timeline() работает с DeadlineEvent без изменений
    print("=== Временная шкала с учётом DeadlineEvent ===")
    print(render_timeline(journal))


    # 2. Фильтрация через именованную функцию (сдачи с баллом >= 85)
    def is_high_score_submission(event: CourseEvent) -> bool:
        return isinstance(event, SubmissionEvent) and event.submission.score >= 85.0


    high_scores_view = FilteredJournalView(journal, is_high_score_submission)

    print("\n=== Сдачи с высоким баллом (именованная функция) ===")
    print(render_timeline(high_scores_view))

    # 3. Фильтрация через lambda (все дедлайны конкретного студента)
    s101_deadlines = FilteredJournalView(
        journal,
        lambda event: isinstance(event, DeadlineEvent) and event.student_id == "s101",
    )

    print("\n=== Дедлайны студента s101 (lambda) ===")
    for event in s101_deadlines:
        print(" ", event.describe())

    # 4. Проверка повторного обхода одного и того же представления
    first_pass = [event.describe() for event in high_scores_view]
    second_pass = [event.describe() for event in high_scores_view]

    print("\n=== Повторный обход FilteredJournalView ===")
    print(f"Первый проход: {len(first_pass)} событий")
    print(f"Второй проход: {len(second_pass)} событий")
    assert first_pass == second_pass