#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    school = {}
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'mod':
            # Запросить данные об изменениях в классе.
            cl = input("Enter class: ")
            students = int(input("Enter number of students: "))

            # Проверка на существование
            if cl in school.keys():
                # Изменяем запись
                school[cl] = students
            else:
                print("Введен несуществующий класс")

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+'.format(
                '-' * 8,
                '-' * 25
            )
            print(line)
            print(
                '| {:^8} | {:^25} |'.format(
                    "Класс",
                    "Количество учащихся"
                )
            )
            print(line)

            # Вывести данные о всех сотрудниках.
            for cl, std in school.items():
                print(
                    '| {:<8} | {:<25} |'.format(
                        cl,
                        std
                    )
                )

            print(line)

        elif command == 'new':
            # Запросить данные о новом классе.
            cl = input("Enter class: ")
            students = int(input("Enter number of students: "))

            # Добавить запись
            school.setdefault(cl, students)

        elif command == 'count':
            # Подсчитаем общее количество учеников
            all_std = sum(s for s in school.values())
            print(f'Total number of students: {all_std}')

        elif command == 'del':
            # Запросить данные о классе.
            cl = input("Enter class: ")
            # Удалить запись
            del school[cl]

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("new - создать запись о новом классе;")
            print("mod - изменить сведения о кол-ве обучающихся;")
            print("del - удалить класс;")
            print("list - вывести список классов;")
            print("count - вывести общее количество учащихся;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
