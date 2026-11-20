from abc import ABC, abstractmethod
from datetime import date, datetime

class CourseEvent(ABC):
    """Общая информация о событиях курса"""
    @property
    def created_at(self) -> datetime:
        """Время создания события (только для чтения)."""
        return self._created_at

    @property
    @abstractmethod
    def student_id(self) -> str:
        """Идентификатор студента, к которому относится событие."""
        ...

    @abstractmethod
    def describe(self) -> str:
        """Человекочитаемое описание события."""
        ...