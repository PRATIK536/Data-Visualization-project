import socket
import argparse
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style
import datetime

def scan_port(ip, port, banner=False):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                service = ""
                if banner:
                    try:
                        sock.send(b'HEAD / HTTP/1.0\r\n\r\n')
                        service = sock.recv(1024).decode(errors='ignore').strip()
                    except:
                        service = "Banner not available"
                output = f"[OPEN] Port {port} - {service}"
                print(Fore.GREEN + output + Style.RESET_ALL)
                return output
            else:
                return None
    except Exception as e:
        print(Fore.YELLOW + f"[!] Error on port {port}: {e}" + Style.RESET_ALL)
        return None

def main():
    parser = argparse.ArgumentParser(description="Expert-Level Python Port Scanner")
    parser.add_argument("ip", help="Target IP address")
    parser.add_argument("start_port", type=int, help="Start port")
    parser.add_argument("end_port", type=int, help="End port")
    parser.add_argument("-t", "--threads", type=int, default=100, help="Number of threads")
    parser.add_argument("-b", "--banner", action="store_true", help="Enable banner grabbing")
    parser.add_argument("-o", "--output", help="Save results to file")

    args = parser.parse_args()
    ip = args.ip
    ports = range(args.start_port, args.end_port + 1)

    print(f"\n Scanning {ip} from port {args.start_port} to {args.end_port}...\n")

    results = []
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = [executor.submit(scan_port, ip, port, args.banner) for port in ports]
        for future in futures:
            result = future.result()
            if result:
                results.append(result)

    if args.output:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{args.output}_{timestamp}.txt"
        with open(filename, "w") as f:
            for line in results:
                f.write(line + "\n")
        print(Fore.CYAN + f"\n Results saved to {filename}" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
    #python expert_port_scanner.py 127.0.0.1 20 100 -b -o scan_results