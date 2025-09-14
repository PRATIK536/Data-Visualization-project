import socket

def scan_available_ports(start_port=1, end_port=1024):
    available_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            # Try binding to localhost on the given port
            sock.bind(('127.0.0.1', port))
            available_ports.append(port)
        except OSError:
            pass  # Port is already in use or restricted
        finally:
            sock.close()

    return available_ports

if __name__ == "__main__":
    print("Scanning for available ports on localhost...")
    free_ports = scan_available_ports(1, 1024)
    print(f"Available ports: {free_ports}")