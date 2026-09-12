from port_scanner import PortScanner

type_scan = input("Enter type scan(s, r): ")
target = input("Enter IP: ").strip()
instance = PortScanner(target)
if type_scan == "s":
    port = int(input("Enter port: "))
    instance.single_scan(port)
elif type_scan == "r":
    begin = int(input("Enter begin port: "))
    end   = int(input("Enter end port: "))
    instance.range_scan(begin, end)