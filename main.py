from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.types import auth
import asyncio
import os

api_id = ''
api_hash = ''
sessions_dir = './sessions'

if not os.path.exists(sessions_dir):
    os.makedirs(sessions_dir)

async def register_and_save_session():
    phone_number = input("Введите номер телефона: ")
    session_name = os.path.join(sessions_dir, phone_number.lstrip('+'))
    client = TelegramClient(
        session_name,
        api_id,
        api_hash,
        device_model="iPhone 13 Pro Max",
        system_version="iOS 15.4",
        app_version="10.10.0"
    )

    await client.connect()

    if not await client.is_user_authorized():
        try:
            sent_code = await client.send_code_request(phone_number)
            print("Код подтверждения отправлен.")

            if isinstance(sent_code.type, auth.SentCodeTypeApp):
                print("Код будет отправлен через приложение Telegram.")
            elif isinstance(sent_code.type, auth.SentCodeTypeSms):
                print("Код будет отправлен через SMS.")
            elif isinstance(sent_code.type, auth.SentCodeTypeCall):
                print("Код будет отправлен через звонок.")
            elif isinstance(sent_code.type, auth.SentCodeTypeFlashCall):
                print("Код будет отправлен через flash call.")
            else:
                print(f"Неизвестный тип кода: {type(sent_code.type)}. Попробуйте снова.")
                return

            code = input("Введите код: ")
            await client.sign_in(phone_number, code)
            print("Авторизация успешна!")
        except SessionPasswordNeededError:
            password = input("Введите пароль двухэтапной аутентификации: ")
            await client.sign_in(password=password)
            print("Авторизация с паролем успешна!")
        except Exception as e:
            if "EMAIL_UNCONFIRMED" in str(e):
                email = input("Введите email для подтверждения: ")
                await client.send_code_request(phone_number, email)
                email_code = input("Введите код из email: ")
                await client.sign_in(phone_number, email_code)
                print("Авторизация через email успешна!")
            else:
                print(f"Ошибка: {e}")
                return

    print(f"Сессия сохранена в {session_name}.session")
    await client.disconnect()

if __name__ == '__main__':
    asyncio.run(register_and_save_session())