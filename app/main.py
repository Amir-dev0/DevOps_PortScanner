import socket
import colorama

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
target = input("Enter IP:  ")


def scan(port):
    try:
        con = sock.connect((target, port))
        return True

    except:
        return False


for x in range(8070, 8090):
    if scan(x):
        print(colorama.Fore.RED + f"[+] port {x} is open")

    else:
        print(colorama.Fore.GREEN + f"[-] port {x} is close")
