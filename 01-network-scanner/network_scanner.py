import socket
import time
import sys
from concurrent.futures import ThreadPoolExecutor

# Liste étendue des ports communs
COMMON_PORTS = {
    21: "FTP", 22: "SSH", 23: "TELNET", 25: "SMTP", 
    53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP", 
    443: "HTTPS", 3306: "MySQL", 5432: "PostgreSQL", 
    8080: "HTTP-ALT"
}

def get_banner(sock):
    """Tente de récupérer la bannière du service pour identification."""
    try:
        # Envoie une petite donnée pour provoquer une réponse du service
        sock.send(b'Hello\r\n')
        return sock.recv(1024).decode().strip()
    except:
        return None

def scan_port(ip, port):
    """Scanne un port spécifique et tente de détecter le service."""
    try:
        # Création du socket avec un timeout court pour la rapidité
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.0) 
        result = sock.connect_ex((ip, port))
        
        if result == 0:
            banner = get_banner(sock)
            sock.close()
            return port, banner
        sock.close()
    except Exception:
        pass
    return None

def main():
    # Interaction utilisateur simple (peut être remplacé par argparse plus tard)
    target_ip = input("Enter target IP: ")
    try:
        start_port = int(input("Start port (ex: 1): "))
        end_port = int(input("End port (ex: 1000): "))
    except ValueError:
        print("Error: Ports must be numbers.")
        sys.exit(1)

    print(f"\n--- Scanning {target_ip} ---")
    start_time = time.time()
    open_ports = []

    # Utilisation du multi-threading pour scanner 100 ports à la fois
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scan_port, target_ip, port) for port in range(start_port, end_port + 1)]
        
        for future in futures:
            res = future.result()
            if res:
                open_ports.append(res)

    # Affichage des résultats
    print(f"\n{'PORT':<10} {'STATUS':<10} {'SERVICE':<15} {'BANNER'}")
    print("-" * 50)
    
    for port, banner in open_ports:
        service = COMMON_PORTS.get(port, "Unknown")
        banner_text = banner if banner else "No banner detected"
        print(f"{port:<10} {'OPEN':<10} {service:<15} {banner_text}")

    end_time = time.time()
    print(f"\nScan finished in {end_time - start_time:.2f} seconds.")
    print(f"Total ports scanned: {end_port - start_port + 1}")
    print(f"Open ports found: {len(open_ports)}")

if __name__ == "__main__":
    main()
