# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Перечислить список команды и написать кто чем занимался вывести колличество и всех разработчиков.
COMANDA = {
    'Эрик': 'Игра',
    'МатвейЧ': 'Видео',
    'Алексей': 'Призентация',
    'МатвейГ': 'Нейронка',
    'Денис': 'Игра'
}


def process_comand(query):
    if query == 'Количество людей':
        count = len(COMANDA)
        return f'В нашей команде {count} людей'
    elif query == 'Список команды':
        work_string = ','.join(COMANDA)
        return f' {work_string}'
    elif query == 'Чем кто занимался':
        unique_work = set(COMANDA.values())
        works_string = ', '.join(unique_work)
        return f'Задача {works_string}'
    else:
        return 'Не понял'


def process_comandos(name, query):
    A = query.split()
    B = A[1:]
    C = ' '.join(B)
    if C == 'Что делаешь?':
        if name in COMANDA.keys():
            return f'{name} занимается {COMANDA[name]}'
        else:
            return f'Такого как {name} нет'
    else:
        return 'Не понял'


def procces_conandes(query):
    name1 = query.split()
    name = name1[0].replace(',', '')
    if name == 'проверка':
        return process_comand(query)
    else:
        return process_comandos(name, query)


print(process_comand('Количество людей'))
print(process_comand('Список команды'))
print(process_comand('Чем кто занимался'))
print(procces_conandes('Алексей, Что делаешь?'))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
