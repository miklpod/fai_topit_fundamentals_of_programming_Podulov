res=int(input())
work=str(input())
skip=int(input())

if res<0 or res>100:
    print("Значение res некорректно")
elif skip<0 or skip>5:
    print("Значение skip некорректно")
else:
    print('Данные skip и res введены корректно')
    skip_flag=0
    if skip>3:
        skip_flag=1
    if res<60:
        level='недостаточный'
    elif res<75:
        if not skip_flag:
            level='удовлетворительный'
        else:
            level = 'недостаточный'
    elif res<90:
        if not skip_flag:
            level='хороший'
        else:
            level = 'удовлетворительный'
    else:
        if not skip_flag:
            level='отличный'
        else:
            level = 'хороший'
    print('уровень:', level)

    match work:
        case 'exam':
            print(work, '— экзаменационная работа')
        case 'project':
            print(work, '— проектная работа')
        case 'practice':
            print(work, '— практическая работа')
        case _:
            print("Значение work некорректно")

students = [
(95, "exam", 1),
(85, "project", 4),
(72, "practice", 2),
(58, "exam", 0),
(60, "project", 5),
(100, "practice", 3),
(75, "exam", 4),
(45, "project", 1),
(90, "practice", 0),
(74, "exam", 3)]

results=[]
level_counter=[0]*4

def stats(score, work_type, absences):
    if score < 0 or score > 100:
        level = None
        type=None
    elif absences < 0 or absences > 5:
        level = None
        type = None
    else:
        absences_flag = 0
        if absences > 3:
            absences_flag = 1
        if score < 60:
            level_counter[0] += 1
            level = 'недостаточный'
        elif score < 75:
            if not absences_flag:
                level_counter[1] += 1
                level = 'удовлетворительный'
            else:
                level_counter[0] += 1
                level = 'недостаточный'
        elif score < 90:
            if not absences_flag:
                level_counter[2] += 1
                level = 'хороший'
            else:
                level_counter[1] += 1
                level = 'удовлетворительный'
        else:
            if not absences_flag:
                level_counter[3] += 1
                level = 'отличный'
            else:
                level_counter[2] += 1
                level = 'хороший'


        match work_type:
            case 'exam':
                type = 'экзаменационная работа'
            case 'project':
                type = 'проектная работа'
            case 'practice':
                type = 'практическая работа'
            case _:
                type = None
    return level, type

for score, work_type, absences in students:
    level, type = stats(score, work_type, absences)
    if level is None or type is None:
        results.append(f"[{score}, {work_type}, {absences}] - {type}")
    else:
        line = f"[{score}, {work_type}, {absences}] - уровень: {level} ({type})"
        results.append(line)

print("Индивидуальные результаты:")
for line in results:
    print(line)

print("\nИтоговая сводка:")
order = ['недостаточный','удовлетворительный','хороший','отличный']
for x in range(len(level_counter)):
    print(f"  {order[x]}: {level_counter[x]}")
print(f"Всего обработано: {len(students)}")