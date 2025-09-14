import socket
import threading

# Target IP (replace with any live IP you want to scan)
target_ip = '127.0.0.1'  # Example: your router or a remote server
start_port = 1
end_port = 1024

# Lock for clean console output
print_lock = threading.Lock()

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout for responsiveness
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            with print_lock:
                print(f"[+] Port {port} is OPEN")
        sock.close()
    except Exception:
        pass

def main():
    print(f"Scanning {target_ip} from port {start_port} to {end_port}...\n")
    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(port,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
   # 127.0.0.1
   #192.168.1.1