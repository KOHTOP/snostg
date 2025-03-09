from telethon import TelegramClient, functions
from telethon.tl.types import InputReportReasonSpam
import asyncio
import os

api_id = ''
api_hash = ''
sessions_dir = './sessions'

if not os.path.exists(sessions_dir):
    print(f"Папка {sessions_dir} не найдена.")
    exit()

sessions = [f for f in os.listdir(sessions_dir) if f.endswith('.session')]

if not sessions:
    print("Нет сохраненных сессий.")
    exit()

target_username = input("Введите username или ID аккаунта, на которого хотите пожаловаться: ")

async def report_account(session_file):
    session_name = os.path.join(sessions_dir, session_file.replace('.session', ''))
    client = TelegramClient(session_name, api_id, api_hash)

    try:
        await client.start()
        print(f"Аккаунт {session_file} загружен.")

        target_entity = await client.get_entity(target_username)

        await client(functions.account.ReportPeerRequest(
            peer=target_entity,
            reason=InputReportReasonSpam(),
            message="Этот аккаунт нарушает правила."
        ))
        print(f"Жалоба от {session_file} отправлена на {target_username}.")
    except Exception as e:
        print(f"Ошибка в аккаунте {session_file}: {e}")
    finally:
        await client.disconnect()

async def main():
    tasks = [report_account(session) for session in sessions]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())