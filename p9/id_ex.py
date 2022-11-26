#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    # Список работников.
    peopls = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о человеке.
            name = input("Фамилия и имя: ")
            phone = int(input("Номер телефона: +7"))
            birthday = list(map(int, input("Дата рождения: ").split('.')))

            # Создать словарь.
            human = {
                'name': name,
                'phone': phone,
                'birthday': birthday
            }

            # Добавить словарь в список.
            peopls.append(human)
            # Отсортировать список в случае необходимости.
            if len(peopls) > 1:
                peopls.sort(key=lambda item: item.get('phone', 0))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 15,
                '-' * 15
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^15} | {:^15} |'.format(
                    "№",
                    "Ф и И.",
                    "Телефон",
                    "День рождения"
                )
            )
            print(line)

            # Вывести данные о всех сотрудниках.
            for idx, human in enumerate(peopls, 1):
                print(
                    '| {:>4} | {:<30} | {:<15} | {:>15} |'.format(
                        idx,
                        human.get('name', ''),
                        human.get('phone', 0),
                        ''.join(str(human.get('birthday')))
                    )
                )

            print(line)

        elif command == 'find':
            f = input('Введите фамилию: ')
            for human in peopls:
                if f in str(human.values()):
                    print('Запись найдена:')
                    print(
                        f"Имя: {human.get('name', '')} \n"
                        f"Номер: {human.get('phone', 0)} \n"
                        f"День рождения: {human.get('birthday', 0)}"

                    )
                    continue
                else:
                    print('Запись не найдена')

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить человека;")
            print("list - вывести список людей;")
            print("find - поиск по фамилии;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
