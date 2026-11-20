from abc import ABC, abstractmethod
from datetime import date, datetime
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


def SubmissionEvent(CourseEvent):
    def __init__(self, submission: Submission):
        super().__init__()
        self.submission = submission
        self.created_at = datetime.now()

    @property
    def student_id(self) -> str:
        return self.submission.student_id
    @property
    def created_at(self) -> datetime:
        return self.submission.created_at
    @property
    def describe(self):
        return f'Студент {self.student_name} сдал {self.submission.laboratory_id}, попытка {self.submission.attempt}. Дата: {self.created_at}'

