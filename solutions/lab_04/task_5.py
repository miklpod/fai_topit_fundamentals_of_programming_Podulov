from abc import ABC, abstractmethod
from datetime import datetime
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
