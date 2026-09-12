import socket
import errno

from app.models.scan import ScanResult
class PortScanner:
    def __init__(self, target):
        self.target = target

    def scan(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.7)
        try:
            result = s.connect_ex((self.target, port))
            if result == 0:
                return ScanResult(
                    target= self.target,
                    port= port,
                    status= "open"
                )
            elif result in (errno.ETIMEDOUT, errno.EAGAIN, errno.EHOSTUNREACH):
                return ScanResult(
                    target= self.target,
                    port= port,
                    status= "timeout"
                )
            else: 
                return ScanResult(
                    target= self.target,
                    port= port,
                    status= "closed"
                )
        except (socket.timeout, TimeoutError):
                return ScanResult(
                    target= self.target,
                    port= port,
                    status= "timeout"
                )
        except OSError:
                return ScanResult(
                    target= self.target,
                    port= port,
                    status= "closed"
                )
        finally:
            s.close()