@echo off
chcp 65001

echo Установка зависимостей...
pip install -r requirements.txt

echo Установка завершена

:question
set /p choice="Запустить основной файл? (y/n): "
if /i "%choice%"=="y" (
    python main.py
) else if /i "%choice%"=="n" (
    exit
) else (
    echo Пожалуйста, введите 'y' или 'n'.
    goto question
)
