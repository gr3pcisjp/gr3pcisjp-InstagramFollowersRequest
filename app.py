import requests
import time
import os
import json
from dotenv import load_dotenv

load_dotenv()

headers = json.loads(os.getenv("HEADERS"))
cookies = json.loads(os.getenv("COOKIES"))

base_url = 'https://www.instagram.com/api/v1/friendships/5645593830/followers/'





params = {
    'count': 120
}

all_users = []
has_more = True
max_id = None

while has_more:
    if max_id:
        params['max_id'] = max_id
    else:
        params.pop('max_id', None)

    response = requests.get(base_url, headers=headers, cookies=cookies, params=params)

    if response.status_code != 200:
        print(f"Ошибка: {response.status_code}")
        print(response.text)
        break

    data = response.json()
    users = data.get('users', [])
    all_users.extend(users)

    for user in users:
        print(user['username'])

    max_id = data.get('next_max_id')
    has_more = bool(max_id)

    # пауза между запросами, чтобы не получить временный бан
    time.sleep(2.5)

print(f"\n✅ Всего загружено пользователей: {len(all_users)}")

with open("followers.txt", "w", encoding="utf-8") as f:
    for user in all_users:
        f.write(user['username'] + "\n")
