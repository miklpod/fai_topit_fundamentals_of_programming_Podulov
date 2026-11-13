from math import ceil
class StepRangeIterator:
    def __init__(self, start, stop, step):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        # Положительный шаг
        if self.step > 0 and self.current >= self.stop:
            raise StopIteration
        # Отрицательный шаг
        elif self.step < 0 and self.current <= self.stop:
            raise StopIteration

        value = self.current
        self.current += self.step
        return value



class StepRange:
    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError("Шаг не может быть равен нулю")

        # Переобозначаем start и stop, если дан только 1 аргумент
        if stop is None:
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop

        self.step = step
    def __iter__(self):
        return StepRangeIterator(self.start, self.stop, self.step)
    def __len__(self):
        if self.step > 0:
            if self.start >= self.stop:
                return 0
            return ceil((self.stop - self.start) / self.step)
        else:
            if self.stop >= self.start:
                return 0
            return ceil((self.start - self.stop) / abs(self.step))
    def __contains__(self, value):
        # Проверяем попадание в границы
        if self.step > 0:
            if not (self.start <= value < self.stop):
                return False
        else:
            if not (self.stop < value <= self.start):
                return False
        # Проверяем кратность шагу (остаток от деления)
        return (value - self.start) % self.step == 0

    def __repr__(self):
        """Строковое представление объекта"""
        return f"StepRange({self.start}, {self.stop}, {self.step})"


print(list(StepRange(0, 5, 1)))
print(len(StepRange(0, 5, 1)))

print(list(StepRange(5, 0, -1)))
print(len(StepRange(5, 0, -1)))

print(list(StepRange(0, 0, 1)))
print(len(StepRange(0, 0, 1)))

print(list(StepRange(0, 5, -1)))
print(len(StepRange(0, 5, -1)))


numbers = StepRange(2, 11, 3)
print(len(numbers))
a=iter(numbers)
b=iter(numbers)

print(next(a))
print(next(b))
print(next(a))
print(next(b))
print(next(a))
print(next(b))

print(StepRange.__contains__(numbers, 5))


def my_enumerate(iterable, start=0):
    a=[]
    it = iter(iterable)
    while True:
        try:
            a.append((start,next(it)))
            start += 1
        except StopIteration:
            return a

print(my_enumerate(StepRange(0, 5, 1)))

def my_zip(first, second):
    first=iter(first)
    second = iter(second)
    a=[]
    while True:
        try:
            a.append((next(first), next(second)))
        except StopIteration:
            return a

print(my_zip(StepRange(0, 5, 1),StepRange(2, 11, 3)))