
# Network Security Scanner v2.0

A high-performance, multi-threaded TCP port scanner written in Python for security auditing and network reconnaissance.

## Key Features
- [cite_start]**Fast Scanning**: Leverages `ThreadPoolExecutor` to scan hundreds of ports concurrently[cite: 2].
- [cite_start]**Service Fingerprinting**: Includes a **Banner Grabbing** engine to attempt identification of the service version running on open ports[cite: 2].
- [cite_start]**Intelligent Mapping**: Matches open ports against an internal database of common network services (SSH, FTP, HTTP, etc.)[cite: 2].
- [cite_start]**Clean Output**: Displays results in a structured table for better readability[cite: 2].
- [cite_start]**Output Parsing**: Clean up banner results by extracting only the server headers or version strings (e.g., "Python/3.10.x" instead of the full HTML body).  

##Technical Implementation
- [cite_start]**Socket Programming**: Low-level TCP connection handling using Python's `socket` library[cite: 2, 3].
- [cite_start]**Concurrency**: Optimized performance using the 'concurrent.futures' module[cite: 2].
- [cite_start]**Error Management**: Robust exception handling to manage timeouts and unreachable hosts[cite: 2].

## Usage
1. Clone the repository:
   ```bash
   git clone [https://github.com/Kaplaka/Network-Scanner.git](https://github.com/Kaplaka/Network-Scanner.git)

2. Run the scanner:
   'bash
  python3 network_scanner.p

2. inter the target IP and range (e.g.,127.0.0.1, start port 1, end port 9000)

3. Output:
PORT       STATUS     SERVICE         BANNER
--------------------------------------------------
22         OPEN       SSH             SSH-2.0-OpenSSH_8.2p1
80         OPEN       HTTP            No banner detected
3306       OPEN       MySQL           5.7.33-0ubuntu0.18.04.1

## Author

Jonas KAPLAKA – Cybersecurity Portfolio Project
