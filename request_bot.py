import requests
import time

API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = '6217012015:AAHxB44gMB4_DZ31SnFW_2E61T8wyaKgC_E'

offset: int = -2
timeout: int = 50
updates: dict


def do_something() -> None:
    print('Update')


while True:
    print('wait')
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something()

    end_time = time.time()
    print(f'Time between Telegram-zaprosami in Bot API: {end_time - start_time}')
