researcher_name = input('Введите Ф.И.О. исследователя:\n')
date = input('Введите дату:\n')
experiment_name = input('Введите наименование эксперимента:\n')
conclusion = input('Введите вывод эксперимента:\n')
line = '—'*71
border = f'+{line}+' 
with open('journal.txt','w',encoding='UTF-8') as file:
    file.write(f'+ {line} +\n')
    file.write('|                      Электронный лабораторный журнал                    |\n')
    file.write(f'+ {line} +\n')
    file.write(f'| Ф.И.О. исследователя: {researcher_name:<{70-len("Ф.И.О. исследователя:")}} |\n')
    file.write(f'| Дата: {date:<{70-len("Дата:")}} |\n')
    file.write(f'| Эксперимент: {experiment_name:<{70-len("Эксперимент:")}} |\n')
    file.write(f'+ {line} +\n')
    file.write(f'| Вывод: {conclusion:<{70-len("Вывод:")}} |\n')
    file.write(f'+ {line} +\n')