#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from datetime import date

def get_train():
    """""
    Запросить данные о рейсе.
    """""
    dist = input("Введите пункт для поезда:  ")
    time = input("Введите время поезда:  ")
    number = int(input("Введите номер поезда:  "))
    return {
        'dist': dist,
        'number': number,
        'time': time,
    }


def display_trains(trains):
    """""
    Отобразить список рейсов
    """""
    # Заголовок таблицы.
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 5,
        '-' * 20,
        '-' * 14,
        '-' * 16
    )
    print(line)
    print(
        '| {:^5} | {:^20} | {:^14} | {:^16} |'.format(
            "№",
            "Едет в",
            "№ поезда",
            "Время отпр-ния"
        )
    )
    print(line)
    # Вывести данные о всех поездах.
    for idx, tr in enumerate(trains, 1):
        print(
            '| {:>5} | {:<20} | {:<14} | {:>16} |'.format(
                idx,
                tr.get('dist', ''),
                tr.get('number', 0),
                tr.get('time', '')
            )
        )
    print(line)


def select_trains(trains, selected_num):
    """""
    Выбрать рейсы с заданным номером
    """""
    # Инициализировать счетчик.
    count = 0
    # Сформировать список поездов
    result = []
    # Проверить сведения работников из списка.
    for tr in trains:
        if tr.get('zodiak', '') == selected_num:
            count += 1
            result.append(tr)

    return result


def help():
    print("Список команд:\n")
    print("[add - добавить рейс]")
    print("[list - вывести список рейсов]")
    print("[select <номер> - запросить рейсы с номером]")
    print("[help - отобразить справку]")
    print("[exit - завершить работу с программой]")


def main():
    """""
    Главная функция программы
    """""
    print("help - список всех команд")
    trains = []
    while True:
        command = input(">>> ").lower()

        if command == "help":
            help()

        elif command == "add":
            train = get_train()
            # Добавить словарь в список.
            trains.append(train)
            # Сортировка в случае необходимости
            if len(trains) > 1:
                trains.sort(key=lambda item: item.get('number', ''))

        elif command == 'list':
            display_trains(trains)

        elif command == 'exit':
            break

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=1)
            selected_num = int(parts[1])
            selected = select_trains(trains, selected_num)
            display_trains(selected)

        else:
            print(f"Неизвестная команда {command}", file = sys.stderr)


if __name__ == '__main__':
    main()
