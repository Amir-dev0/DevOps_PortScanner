import colorama

from app.port_scanner import PortScanner
from colorama import Fore, Style

colorama.init()

type_scan = input("Enter type scan(s, r): ")
target = input("Enter IP: ").strip()
instance = PortScanner(target)

if type_scan == "s":
    port = int(input("Enter port: "))
    result = instance.scan(port)

    if result.status == "open":
        print(Fore.RED + f"[+] port {port} is open" + Style.RESET_ALL)
    elif result.status == "timeout":
        print(Fore.LIGHTBLACK_EX + f"[?] port {port} timeout (filtered)" + Style.RESET_ALL)
    elif result.status == "closed":
        print(Fore.GREEN + f"[-] port {port} is closed" + Style.RESET_ALL)

elif type_scan == "r":
    begin = int(input("Enter begin: "))
    end = int(input("Enter end: "))

    for port in range(begin, end+1):
        result = instance.scan(port)
        if result.status == "open":
            print(Fore.RED + f"[+] port {port} is open" + Style.RESET_ALL)
        elif result.status == "timeout":
            print(Fore.LIGHTBLACK_EX + f"[?] port {port} timeout (filtered)" + Style.RESET_ALL)
        elif result.status == "closed":
            print(Fore.GREEN + f"[-] port {port} is closed" + Style.RESET_ALL)