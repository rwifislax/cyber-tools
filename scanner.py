from queue import PriorityQueue, Queue
import socket
import threading


def portscan(port):
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        sock.connect((target, port))
        return True
    except:
        return False


def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open!".format(port))
            open_ports.append(port)


def run_scanner(threads, mode):

    get_ports(mode)

    thread_list = []

    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    print()
    print("********SUMMARY*********")
    print("Open ports are:", open_ports)

def get_ports(mode):
    if mode == 1:
        for port in range(1, 1025):
            queue.put(port)
    elif mode == 2:
        for port in range(1, 65536):
            queue.put(port)
    elif mode == 3:
        ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]
        for port in ports:
            queue.put(port)
    elif mode == 4:
        ports = input("Enter your ports (seperate by blank):")
        ports = ports.split()
        ports = list(map(int, ports))
        for port in ports:
            queue.put(port)

def main():
    
    global target,queue,open_ports,closed_ports
    #Global variables
    queue = Queue()
    open_ports = []
    closed_ports = []

    option = ['1','2','3','4']
    
    target = input("Input an IP address to scan: ")

    while True:
        print("Select a mode")
        print("1. 1024 ports\n2. 65535\n3. most common\n4. Enter your own ports")
        mode = input()
        
        if mode in option:
            mode = int(mode)
            break
        else:
            print("Type a valid option\n")

    #Execute scanner with 100 threats
    run_scanner(100, mode)

if __name__ == '__main__':
    main()
