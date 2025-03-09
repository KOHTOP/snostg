from telethon import TelegramClient, events
import asyncio
import os
import re

api_id = ''
api_hash = ''
sessions_dir = './sessions'

sessions = [f for f in os.listdir(sessions_dir) if f.endswith('.session')]

if not sessions:
    print("Нет сохраненных сессий. Сначала зарегистрируйте аккаунты.")
    exit()

print("Доступные аккаунты:")
for i, session in enumerate(sessions):
    print(f"{i + 1}. {session}")

choice = int(input("Выберите аккаунт (введите номер): ")) - 1
if choice < 0 or choice >= len(sessions):
    print("Неверный выбор.")
    exit()

session_name = os.path.join(sessions_dir, sessions[choice].replace('.session', ''))
client = TelegramClient(session_name, api_id, api_hash)

async def parse_messages():
    await client.start()
    print(f"Аккаунт {session_name} успешно загружен. Ожидание сообщений...")

    @client.on(events.NewMessage)
    async def handler(event):
        message = event.message.message
        code_matches = re.findall(r'\b\d{4,6}\b', message)
        if code_matches:
            for code in code_matches:
                print(f"Найден код: {code}")

    await client.run_until_disconnected()

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(parse_messages())