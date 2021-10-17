import time
from dirsync import sync
import logging
import argparse
import sys
import datetime


def create_parser():  # Функция парсинга аргументов командной строки
    parse = argparse.ArgumentParser()
    parse.add_argument('-s', '--source')
    parse.add_argument('-r', '--replica')
    parse.add_argument('-int', '--interval')
    parse.add_argument('-lp', '--log_path')
    return parse


def copy_catalog():  # Функция синхронизации каталога

    # Создание пространства имен аргументов командной строки
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])

    if namespace.source and namespace.replica and namespace.log_path and namespace.interval:

        # Очистка логов
        log = open(namespace.log_path, "w")
        log.write("")
        log.close()

        # Привязка путей к переменным
        path1 = namespace.source
        path2 = namespace.replica

        # Настройка логгера для вывода в лог файл
        logging.basicConfig(filename=namespace.log_path, filemode='a', format='%(message)s')

        # Начало цикла синхронизации
        while True:

            # Запись в лог файл времени начала синхронизации
            log = open(namespace.log_path, "a")
            log.write("Begin synchronisation time: " + datetime.datetime.now().strftime("%H:%M") + "\n")
            log.close()

            # Синхронизация
            sync(path1, path2, 'sync', purge=True)

            # Уснуть на введенный интервал
            time.sleep(int(namespace.interval))
    else:
        print("Invalid args")


if __name__ == "__main__":
    copy_catalog()
