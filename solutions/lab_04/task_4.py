from dataclasses import dataclass

@dataclass
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


class Student:
    def __init__(self, student_id: str, attempts: list, student_name: str) -> None:
        self.student_id = student_id
        self.attempts = attempts
        self.student_name = student_name