# Описание проекта

Этот проект предоставляет инструменты для управления сессиями, автоматической подачи жалоб и парсинга сообщений. Ниже приведено описание файлов и инструкции по установке.

---

## 📂 Описание файлов

### 1. **main.py**
   - Позволяет добавлять сессии.
   - Запрашивает код для входа и сохраняет сессию для дальнейшей работы.

### 2. **session.py**
   - Получает код для входа, если вы были выкинуты или случайно вышли.
   - Парсит сообщения с возможным кодом (от 4 до 6 символов) из любых сообщений.

### 3. **snos.py**
   - Используется для подачи жалоб.
   - Вводите username человека, и все ваши сессии автоматически подают на него жалобу.

### 4. **requirements.txt**
   - Содержит список необходимых библиотек для работы проекта.

### 5. **setup.bat**
   - Автоматически устанавливает все необходимые библиотеки.
   - Если вы нажмете `Y`, то запустится `main.py`.

---

## 🛠️ Установка

1. Скачайте или клонируйте репозиторий.
2. Запустите `setup.bat` для установки всех необходимых библиотек.
3. Следуйте инструкциям в `main.py` для добавления сессий и начала работы.

---

## ⚠️ Важно

Используйте данный скрипт ответственно и в соответствии с правилами и условиями платформы, на которой вы работаете. Неправомерное использование может привести к блокировке аккаунтов.

---

## 📜 Лицензия

Этот проект не имеет лицензии. Используйте на свой страх и риск.

---
