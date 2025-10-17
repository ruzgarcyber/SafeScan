import requests
from colorama import init, Fore, Style

init(autoreset=True)

SUPHELİLER = {"malicious.com", "phishy.net", "badsite.org"}

def get_requests(url):
    try:
        r = requests.get(url, timeout=5)
        print(f"{Fore.GREEN}GET isteği gönderildi - Status: {r.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}HATA: {e}")

def scan_url(url):
    if url.startswith("https://"):
        print(f"{Fore.GREEN}HTTPS: VAR")
    else:
        print(f"{Fore.RED}HTTPS: YOK")

    for blocked in SUPHELİLER:
        if blocked in url:
            print(f"{Fore.RED}Uyarı: URL blacklist ile eşleşiyor ({blocked})")
            break
    else:
        print(f"{Fore.GREEN}Blacklist ile eşleşme yok")

if __name__ == "__main__":
    URL = input("İstediğiniz bir URL girin: ").strip()
    scan_url(URL)
    get_requests(URL)