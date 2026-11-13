students = {
    "Анна": [78, 91, 84, 88],
    "Борис": [60, 72, 68],
    "Дарья": [95, 93, 97, 90],
    "Илья": [55, 61],
}

no_res = "Нет результатов"


def mean(values):
    """Вход: список чисел. Результат: среднее. Пустой список -> None."""
    if not values:
        return None
    return sum(values) / len(values)


def minimum(values):
    """Вход: список чисел. Результат: наименьшее. Пустой список -> None."""
    if not values:
        return None
    result = values[0]
    for value in values:
        if value < result:
            result = value
    return result


def maximum(values):
    """Вход: список чисел. Результат: наибольшее. Пустой список -> None."""
    if not values:
        return None
    result = values[0]
    for value in values:
        if value > result:
            result = value
    return result


def classify(score):
    """Вход: число (среднее) или None. Результат: название категории.
    Границы: 90 и выше, 75 и выше, 60 и выше. None -> 'Нет результатов'."""
    if score is None:
        return no_res
    if score >= 90:
        return "Отлично"
    if score >= 75:
        return "Хорошо"
    if score >= 60:
        return "Удовлетворительно"
    return "Неудовлетворительно"


def student_summary(name, results):
    """Вход: имя и список результатов. Результат: словарь с итогами студента.
    Пустой список: count = 0, mean/min/max = None, категория 'Нет результатов'."""
    average = mean(results)
    return {
        "name": name,
        "count": len(results),
        "mean": average,
        "min": minimum(results),
        "max": maximum(results),
        "category": classify(average),
    }


def find_top_students(students):
    """Вход: словарь {имя: список результатов}. Результат: список имён с наибольшим средним.
    Студенты без результатов не участвуют. Нет подходящих студентов -> []."""
    means = {}
    for name, results in students.items():
        if results:
            means[name] = mean(results)
    if not means:
        return []
    best = maximum(list(means.values()))
    top = []
    for name, value in means.items():
        if value == best:
            top.append(name)
    return top


def group_summary(students):
    """Вход: словарь {имя: список результатов}. Результат: словарь со статистикой группы.
    Общее среднее считается по всем результатам всех студентов.
    Пустая группа или нет результатов: mean = None, счётчики = 0."""
    category_counts = {
        "Отлично": 0,
        "Хорошо": 0,
        "Удовлетворительно": 0,
        "Неудовлетворительно": 0,
        no_res: 0,
    }
    total = 0
    count = 0
    for results in students.values():
        category_counts[classify(mean(results))] += 1
        total += sum(results)
        count += len(results)

    group_mean = None
    if count > 0:
        group_mean = total / count

    return {
        "student_count": len(students),
        "result_count": count,
        "mean": group_mean,
        "category_counts": category_counts,
        "top_students": find_top_students(students),
    }


def show(value):
    """Число -> строка с одним знаком после запятой; None -> прочерк."""
    if value is None:
        return "-"
    return f"{value:.1f}"


def format_report(student_data, group_data):
    """Вход: список итогов студентов (student_summary) и итоги группы (group_summary).
    Результат: текст отчёта. Исходные данные не изменяются (рейтинг строится копией)."""
    with_results = []
    without_results = []
    for item in student_data:
        if item["mean"] is None:
            without_results.append(item["name"])
        else:
            with_results.append(item)

    ranking = sorted(with_results, key=lambda item: item["mean"], reverse=True)

    lines = [
        "Отчёт по группе",
        f"Студентов: {group_data['student_count']}, результатов: {group_data['result_count']}",
        f"Общий средний результат: {show(group_data['mean'])}",
        "",
        "Рейтинг по среднему результату:",
    ]
    for place, item in enumerate(ranking, start=1):
        lines.append(
            f"{place}. {item['name']}: среднее {show(item['mean'])}, "
            f"мин {item['min']}, макс {item['max']}, {item['category']}"
        )

    lines.append("")
    lines.append("Без результатов: " + (", ".join(without_results) or "нет"))
    lines.append("")
    lines.append("Количество студентов по категориям:")
    for category, number in group_data["category_counts"].items():
        lines.append(f"{category}: {number}")

    lines.append("")
    lines.append("Лидеры: " + (", ".join(group_data["top_students"]) or "нет"))
    return "\n".join(lines)


def build_report(data):
    """Собирает отчёт для словаря {имя: список результатов}."""
    student_data = [student_summary(name, results) for name, results in data.items()]
    return format_report(student_data, group_summary(data))


def run_checks():
    # 1. Обычный набор данных
    snapshot = {name: results.copy() for name, results in students.items()}
    group = group_summary(students)
    assert group["student_count"] == 4
    assert group["result_count"] == 13
    assert round(group["mean"], 2) == 79.38
    assert group["top_students"] == ["Дарья"]
    assert group["category_counts"]["Отлично"] == 1
    assert group["category_counts"]["Хорошо"] == 1
    assert group["category_counts"]["Удовлетворительно"] == 1
    assert group["category_counts"]["Неудовлетворительно"] == 1
    anna = student_summary("Анна", students["Анна"])
    assert (anna["mean"], anna["min"], anna["max"]) == (85.25, 78, 91)
    assert students == snapshot  # исходный словарь не изменён

    # 2. Один студент
    one = {"Вера": [80, 100]}
    assert group_summary(one)["top_students"] == ["Вера"]
    assert group_summary(one)["mean"] == 90.0
    assert student_summary("Вера", one["Вера"])["category"] == "Отлично"

    # 3. Несколько лидеров (одинаковое среднее 90)
    tie = {"А": [90, 90], "Б": [80, 100], "В": [70]}
    assert find_top_students(tie) == ["А", "Б"]

    # 4. Пустая группа
    empty = {}
    empty_group = group_summary(empty)
    assert empty_group["student_count"] == 0
    assert empty_group["mean"] is None
    assert empty_group["top_students"] == []
    assert "Лидеры: нет" in build_report(empty)

    # 5. Студент без результатов
    partly = {"А": [], "Б": [80]}
    assert student_summary("А", [])["mean"] is None
    assert student_summary("А", [])["category"] == no_res
    assert find_top_students(partly) == ["Б"]
    assert group_summary(partly)["mean"] == 80.0
    assert group_summary(partly)["category_counts"][no_res] == 1

    # 6. Границы категорий
    assert classify(90) == "Отлично"
    assert classify(89.99) == "Хорошо"
    assert classify(75) == "Хорошо"
    assert classify(74.99) == "Удовлетворительно"
    assert classify(60) == "Удовлетворительно"
    assert classify(59.99) == "Неудовлетворительно"
    assert classify(0) == "Неудовлетворительно"

    # 7. minimum / maximum
    assert minimum([5, 2, 9]) == 2
    assert maximum([5, 2, 9]) == 9
    assert minimum([7]) == 7 and maximum([7]) == 7
    assert minimum([]) is None and maximum([]) is None


print(build_report(students))
run_checks()
print("Все сценарии проверки пройдены.")