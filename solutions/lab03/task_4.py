import math

def arithmetic_mean(values: list[float]) -> float:
    """Возвращает среднее арифметическое непустого списка."""
    if not values:
        # Пустой список
        return float("nan")
    return sum(values) / len(values)


def normalize_name(name: str) -> str:
    """Удаляет лишние пробелы и приводит каждую часть имени к нужному регистру."""
    parts = name.split()  # Убираем лишние пробелы
    if not parts:
        return ""
    # В каждой части первая буква заглавная, остальные строчные.
    # Дефисные имена обрабатываются по частям
    normalized = ["-".join(piece.capitalize() for piece in part.split("-")) for part in parts]
    return " ".join(normalized)


def build_report(
    student: str,
    results: list[int],
    *,
    precision: int = 2,
    prefix: str = "Результат",
) -> str:
    """Формирует строковый отчет о результатах студента."""
    name = normalize_name(student)
    if not results:
        return f"{prefix}: {name} - нет результатов"
    mean = arithmetic_mean(results)
    return (
        f"{prefix}: {name} - среднее {mean:.{precision}f}, "
        f"результатов: {len(results)}, "
        f"мин {min(results)}, макс {max(results)}"
    )


def collect_tags(*tags: str, lowercase: bool = True) -> tuple[str, ...]:
    """Возвращает очищенные теги без пустых значений и повторов."""
    seen: set[str] = set()
    cleaned: list[str] = []
    for tag in tags:
        value = tag.strip()
        if not value:
            continue
        if lowercase:
            value = value.lower()
        if value in seen:
            continue
        seen.add(value)
        cleaned.append(value)
    return tuple(cleaned)


course = "Основы программирования"  # глобальное имя (область Global)


def outer_function() -> int:
    """Внешняя функция: владеет именем counter, вложенная функция его изменяет."""
    counter = 0  # локальное имя outer_function; для inner_function оно объемлющее (Enclosing)

    def inner_function() -> str:
        nonlocal counter  # counter ищется во вложенной области, локальное не создаётся
        counter += 1  # меняется связывание имени counter в outer_function
        title = f"{course}: вызов {counter}"  # course только читается, найдено в G
        return title

    first = inner_function()
    second = inner_function()
    print(first)
    print(second)
    print("длина заголовка:", len(second))  # len - встроенное имя (Built-in)
    return counter


def run_scope_asserts() -> None:
    original_course = course
    assert outer_function() == 2  # nonlocal изменил counter внутри outer_function
    assert outer_function() == 2  # новый вызов создаёт новое окружение, счёт заново
    assert course == original_course  # глобальное имя не изменено
    assert "counter" not in globals()  # nonlocal не создал глобальное имя
    assert "inner_function" not in globals()  # вложенная функция видна только внутри


def run_asserts() -> None:
    # arithmetic_mean
    nums = [4, 5, 3]
    snapshot = nums.copy()
    assert arithmetic_mean(nums) == 4.0
    assert arithmetic_mean([2.5]) == 2.5
    assert math.isnan(arithmetic_mean([]))
    assert nums == snapshot  # входной список не изменён

    # normalize_name
    assert normalize_name("  иВАНов   иван  ") == "Иванов Иван"
    assert normalize_name("анна-мария   петрова") == "Анна-Мария Петрова"
    assert normalize_name("   ") == ""
    assert normalize_name("") == ""

    # build_report
    res = [5, 4, 4]
    res_snapshot = res.copy()
    assert build_report("иванов иван", res) == ("Результат: Иванов Иван - среднее 4.33, результатов: 3, мин 4, макс 5")
    assert build_report("иванов иван", res, precision=0) == ("Результат: Иванов Иван - среднее 4, результатов: 3, мин 4, макс 5")
    assert build_report("иванов иван", res, prefix="Итог", precision=1) == ("Итог: Иванов Иван - среднее 4.3, результатов: 3, мин 4, макс 5")
    assert build_report("иванов иван", []) == "Результат: Иванов Иван - нет результатов"
    assert res == res_snapshot
    # precision и prefix — только именованные:
    try:
        build_report("иванов", res, 3)
    except TypeError:
        pass
    else:
        raise AssertionError("precision не должен приниматься позиционно")

    # collect_tags
    assert collect_tags(" Python ", "python", "", "  ", "OOP") == ("python", "oop")
    assert collect_tags("A", "a", "B", lowercase=False) == ("A", "a", "B")
    assert collect_tags() == ()
    assert collect_tags("x", "y", "x") == ("x", "y")
    assert isinstance(collect_tags("x"), tuple)


def demo() -> None:
    print("=== Позиционные и именованные аргументы ===")
    print('arithmetic_mean от [4, 5, 3] =',arithmetic_mean([4, 5, 3]))
    print(normalize_name("  пЕТРОВ   пётр "))
    print(build_report("сидорова анна", [5, 4, 5]))                                  # только позиционные
    print(build_report("сидорова анна", [5, 4, 5], precision=1, prefix="Итог"))     # позиционные + именованные
    print(build_report(student="сидорова анна", results=[5, 4, 5]))                 # обязательные по имени
    print(collect_tags("Python", " python ", "ООП", lowercase=False))

    print("=== Распаковка * (список) ===")
    tag_list = ["Python", " python", "", "Memory", "gc"]
    print(collect_tags(*tag_list))          # каждый элемент списка -> отдельный аргумент
    values = [3, 4, 5]
    print(build_report("иванов иван", values))
    print(arithmetic_mean([*values, 6]))    # распаковка при построении нового списка

    print("=== Распаковка ** (словарь) ===")
    options = {"precision": 3, "prefix": "Оценка"}
    print(build_report("иванов иван", values, **options))
    full = {"student": "петров пётр", "results": [2, 3], "precision": 0}
    print(build_report(**full))
    print(collect_tags(*tag_list, **{"lowercase": False}))

    print("\n=== Области видимости (LEGB, nonlocal) ===")
    final_counter = outer_function()
    print("counter после двух вызовов inner_function:", final_counter)
    print("глобальный course без изменений:", course)

run_asserts()
run_scope_asserts()
print("Все assert-проверки пройдены")
demo()

