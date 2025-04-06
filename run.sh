#!/bin/bash

# Активируем глобальное окружение
source ~/.global-python/bin/activate

# Переходим в папку проекта (если скрипт вызван откуда-то ещё)
cd "$(dirname "$0")"

# Запускаем скрипт
python app.py
