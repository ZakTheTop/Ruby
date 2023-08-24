import random

headers_useragents = list()


def useragent_list():
    global headers_useragents
    with open("UserAgent.txt", "r") as file:
        data = file.readlines()
    for line in data:
        headers_useragents.append(line[:-2])

def randomString(size: int) -> str:
    out_str = ''

    for i in range(0, size):
        a = random.randint(65, 90)
        out_str += chr(a)

    return (out_str)


def initHeaders():
    useragent_list()
    global headers_useragents
    headers = {
        'User-Agent': random.choice(headers_useragents),
        'Cache-Control': 'no-cache',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
        'Referer': 'http://www.google.com/?q=' + randomString(random.randint(5, 10)),
        'Keep-Alive': str(random.randint(110, 120)),
        'Connection': 'keep-alive'
    }
    #print(headers)
    return headers
