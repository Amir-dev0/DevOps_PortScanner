import socket
import colorama
import errno
from colorama import Fore, Style

colorama.init()

class PortScanner():
    def __init__(self, target):
        self.target = target

    def scan(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.7)
        try:
            result = s.connect_ex((self.target, port))
            if result == 0:
                return "open"
            elif result in (errno.ETIMEDOUT, errno.EAGAIN, errno.EHOSTUNREACH):
                return "timeout"
            else: 
                return "closed"
        except (socket.timeout, TimeoutError):
            return "timeout"
        except OSError:
            return "closed"
        finally:
            s.close()
    def single_scan(self, port):
        status = self.scan(port)
        if status == "open":
            print(Fore.RED + Style.BRIGHT + f"[+] port {port} is open" + Style.RESET_ALL)
        elif status == "closed":
            print(Fore.GREEN + f"[-] port {port} is closed" + Style.RESET_ALL)
        else:
            print(Fore.LIGHTBLACK_EX + f"[?] port {port} timeout (filtered)" + Style.RESET_ALL)

    def range_scan(self, begin, end):
        for port in range(begin, end + 1):
            status = self.scan(port)
            if status == "open":
                print(Fore.RED + Style.BRIGHT + f"[+] port {port} is open" + Style.RESET_ALL)
            elif status == "closed":
                print(Fore.GREEN + f"[-] port {port} is closed" + Style.RESET_ALL)
            else:
                print(Fore.LIGHTBLACK_EX + f"[?] port {port} timeout (filtered)" + Style.RESET_ALL)
            