import asyncio
import aiohttp

from providers.free_proxy_list import free_proxy_list_request
from providers.hidemy import hidemy_request


URL = "https://suchen.mobile.de/auto-inserat/su/350943587.html"
HEADERS =  {"User-Agent": "Mozilla/5.0 (Android 8.0.0; Mobile; rv:59.0.2) Gecko/59.0.2 Firefox/59.0.2"}
PROXY_TYPE = "http"
TIMEOUT_SECONDS = 4
ALL_PROXIES: list[str] = []
VALID_PROXIES: list[str] = []

TASKS: list = []


def append_free_proxy_list_proxies() -> list[str]:
    for proxy in free_proxy_list_request():
        ALL_PROXIES.append(f"{proxy.ip}:{proxy.port}")
            

def append_hidemy_proxies() -> list[str]:
    for proxy in hidemy_request():
        ALL_PROXIES.append(f"{proxy.ip}:{proxy.port}")
            
append_free_proxy_list_proxies()
    

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    

async def is_bad_proxy(ipport):
    try:
        proxy = f"{PROXY_TYPE}://{ipport}"
        async with aiohttp.ClientSession(headers=HEADERS) as session:
            async with session.get(URL, proxy=proxy, timeout=TIMEOUT_SECONDS) as response:
                if response.status == 200:
                    print(bcolors.OKBLUE + "Working:", ipport + bcolors.ENDC)
                    VALID_PROXIES.append(ipport)
                else:
                    print(bcolors.FAIL + f"Not working: {ipport}, status: {response.status}" + bcolors.ENDC)
            
    except:
        print(bcolors.FAIL + f"Not Working: {ipport}" + bcolors.ENDC)



def get_tasks():
    for proxy in ALL_PROXIES:
        TASKS.append(asyncio.ensure_future(is_bad_proxy(proxy)))


def main():
    loop = asyncio.get_event_loop()

    print(bcolors.HEADER + "Starting... \n" + bcolors.ENDC)
    get_tasks()
    loop.run_until_complete(asyncio.wait(TASKS))
    print(bcolors.HEADER + "\n...Finished" + bcolors.ENDC)
    print(bcolors.OKBLUE + f"Valid proxies: {VALID_PROXIES}" + bcolors.ENDC)

    return VALID_PROXIES

if __name__ == "__main__":
    main()
