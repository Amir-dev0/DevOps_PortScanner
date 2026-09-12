import socket
import errno

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