# Catalog synchronization
Аргументы CMD:

-s/--source " *path to source catalog* "   -- Путь до исходного каталога

-r/--replica " *path to replica catalog* " -- Путь до каталога реплики

-int/--interval X   -- Интервал синхронизации

-lp/--log_path " *path to log file* " -- Путь до файла логов, можно просто log.txt

HOWTO:

- Открыть main.py с прописанными аргументами. Все аргументы обязательные.

Начнется синхронизация каталогов.
Все изменения файлов можно прочитать в логе
