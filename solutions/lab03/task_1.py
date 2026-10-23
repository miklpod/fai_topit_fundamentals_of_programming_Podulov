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
