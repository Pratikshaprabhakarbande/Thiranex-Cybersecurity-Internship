#!/usr/bin/env python3
"""
Vulnerability Scanner - A beginner-friendly network security scanner
Scans for open ports and detects common vulnerabilities
"""

import socket
import sys
import threading
import time
from datetime import datetime
from typing import Dict, List, Tuple

# Color codes for terminal output (optional feature)
class Colors:
    """Color codes for terminal output"""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'


# Dictionary of common vulnerable ports and their services
VULNERABLE_PORTS = {
    21: {"service": "FTP", "vulnerability": "Unencrypted file transfer - use SFTP instead", "severity": "HIGH"},
    23: {"service": "Telnet", "vulnerability": "Unencrypted remote access - use SSH instead", "severity": "CRITICAL"},
    25: {"service": "SMTP", "vulnerability": "Unencrypted email - consider encrypted alternatives", "severity": "MEDIUM"},
    53: {"service": "DNS", "vulnerability": "May allow DNS enumeration - restrict query types", "severity": "MEDIUM"},
    80: {"service": "HTTP", "vulnerability": "Unencrypted web traffic - use HTTPS", "severity": "HIGH"},
    110: {"service": "POP3", "vulnerability": "Unencrypted email - use TLS/SSL", "severity": "HIGH"},
    143: {"service": "IMAP", "vulnerability": "Unencrypted email - use TLS/SSL", "severity": "HIGH"},
    443: {"service": "HTTPS", "vulnerability": "Secure web traffic (needs certificate validation)", "severity": "LOW"},
    445: {"service": "SMB", "vulnerability": "File sharing - restrict to trusted networks", "severity": "HIGH"},
    3306: {"service": "MySQL", "vulnerability": "Database - must not be exposed to internet", "severity": "CRITICAL"},
    3389: {"service": "RDP", "vulnerability": "Remote desktop - restrict access, use strong passwords", "severity": "CRITICAL"},
    5432: {"service": "PostgreSQL", "vulnerability": "Database - must not be exposed to internet", "severity": "CRITICAL"},
    5900: {"service": "VNC", "vulnerability": "Remote access - use SSH tunneling", "severity": "HIGH"},
    8080: {"service": "HTTP Proxy", "vulnerability": "Proxy service - check firewall rules", "severity": "MEDIUM"},
    27017: {"service": "MongoDB", "vulnerability": "Database - must not be exposed to internet", "severity": "CRITICAL"},
}

# Standard ports for banner grabbing
BANNER_PORTS = {21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 80: "HTTP"}


def print_header():
    """Display a welcome header"""
    print(f"\n{Colors.CYAN}{Colors.BOLD}")
    print("=" * 60)
    print("     VULNERABILITY SCANNER - Port Scanner & Detector")
    print("     A Beginner-Friendly Security Tool")
    print("=" * 60)
    print(f"{Colors.RESET}\n")


def print_colored(text: str, color: str = Colors.WHITE):
    """Print colored text to terminal"""
    print(f"{color}{text}{Colors.RESET}")


def is_valid_ip_or_hostname(target: str) -> bool:
    """
    Validate if the input is a valid IP address or hostname
    
    Args:
        target: IP address or hostname to validate
        
    Returns:
        True if valid, False otherwise
    """
    # Try to resolve hostname/IP
    try:
        socket.gethostbyname(target)
        return True
    except socket.gaierror:
        return False


def resolve_hostname(hostname: str) -> str:
    """
    Convert hostname to IP address
    
    Args:
        hostname: Hostname or IP address
        
    Returns:
        IP address as string
    """
    try:
        ip = socket.gethostbyname(hostname)
        return ip
    except socket.gaierror:
        return None


def grab_banner(host: str, port: int) -> str:
    """
    Attempt to grab banner/service information from an open port
    
    Args:
        host: Target IP address
        port: Port number to connect to
        
    Returns:
        Banner information or empty string if unavailable
    """
    try:
        # Create a socket connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # 2 second timeout
        
        # Try to connect
        sock.connect((host, port))
        
        # Try to receive banner data
        banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
        sock.close()
        
        return banner if banner else ""
    except:
        return ""


def scan_port(host: str, port: int) -> Tuple[int, str]:
    """
    Scan a single port on the target host
    
    Args:
        host: Target IP address
        port: Port number to scan
        
    Returns:
        Tuple of (port, status) - status is 'Open' or 'Closed'
    """
    try:
        # Create a socket using IPv4 and TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout for the connection attempt
        sock.settimeout(1)
        
        # Try to connect to the port
        result = sock.connect_ex((host, port))
        sock.close()
        
        # If connection successful (result == 0), port is open
        if result == 0:
            return (port, "Open")
        else:
            return (port, "Closed")
    except socket.gaierror:
        print_colored(f"[ERROR] Hostname could not be resolved: {host}", Colors.RED)
        sys.exit()
    except socket.error:
        print_colored(f"[ERROR] Could not connect to {host}", Colors.RED)
        sys.exit()


def scan_port_range(host: str, port_range: List[int], show_closed: bool = False) -> Dict:
    """
    Scan a range of ports using threading for faster scanning
    
    Args:
        host: Target IP address
        port_range: List of ports to scan
        show_closed: Whether to show closed ports in results
        
    Returns:
        Dictionary with results
    """
    open_ports = []
    closed_ports = []
    
    print_colored(f"\n[*] Starting port scan on {host}...", Colors.BLUE)
    print_colored(f"[*] Scanning {len(port_range)} ports...\n", Colors.BLUE)
    
    # Scan each port
    for port in port_range:
        port_num, status = scan_port(host, port)
        
        if status == "Open":
            open_ports.append(port_num)
            print_colored(f"[+] Port {port_num}: {status}", Colors.GREEN)
        elif show_closed:
            closed_ports.append(port_num)
            print_colored(f"[-] Port {port_num}: {status}", Colors.YELLOW)
    
    return {"open": open_ports, "closed": closed_ports}


def analyze_vulnerabilities(host: str, open_ports: List[int]) -> List[Dict]:
    """
    Analyze open ports for known vulnerabilities
    
    Args:
        host: Target IP address
        open_ports: List of open ports
        
    Returns:
        List of vulnerability findings
    """
    vulnerabilities = []
    
    print_colored(f"\n[*] Analyzing vulnerabilities...\n", Colors.BLUE)
    
    for port in open_ports:
        if port in VULNERABLE_PORTS:
            vuln_info = VULNERABLE_PORTS[port]
            
            # Attempt banner grabbing
            banner = grab_banner(host, port)
            
            vulnerability = {
                "port": port,
                "service": vuln_info["service"],
                "vulnerability": vuln_info["vulnerability"],
                "severity": vuln_info["severity"],
                "banner": banner
            }
            vulnerabilities.append(vulnerability)
            
            # Display vulnerability with color coding based on severity
            if vuln_info["severity"] == "CRITICAL":
                color = Colors.RED
            elif vuln_info["severity"] == "HIGH":
                color = Colors.YELLOW
            else:
                color = Colors.CYAN
            
            print_colored(f"[!] Port {port} ({vuln_info['service']}) - Severity: {vuln_info['severity']}", color)
            print_colored(f"    ├─ Issue: {vuln_info['vulnerability']}", color)
            if banner:
                print_colored(f"    └─ Banner: {banner[:50]}...", Colors.BOLD)
            print()
    
    return vulnerabilities


def generate_report(host: str, hostname: str, scan_results: Dict, vulnerabilities: List[Dict], scan_time: float) -> str:
    """
    Generate a vulnerability report in text format
    
    Args:
        host: Target IP address
        hostname: Original hostname/IP provided
        scan_results: Results from port scanning
        vulnerabilities: List of vulnerabilities found
        scan_time: Time taken for the scan
        
    Returns:
        Report as string
    """
    report = []
    report.append("=" * 70)
    report.append("VULNERABILITY SCANNER REPORT")
    report.append("=" * 70)
    report.append(f"\nScan Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append(f"Target: {hostname} ({host})")
    report.append(f"Scan Duration: {scan_time:.2f} seconds")
    report.append(f"Total Ports Scanned: {len(scan_results['open']) + len(scan_results['closed'])}")
    report.append(f"Open Ports Found: {len(scan_results['open'])}")
    report.append(f"Vulnerabilities Detected: {len(vulnerabilities)}")
    
    # Summary by severity
    critical = sum(1 for v in vulnerabilities if v['severity'] == 'CRITICAL')
    high = sum(1 for v in vulnerabilities if v['severity'] == 'HIGH')
    medium = sum(1 for v in vulnerabilities if v['severity'] == 'MEDIUM')
    low = sum(1 for v in vulnerabilities if v['severity'] == 'LOW')
    
    report.append(f"\nVulnerability Summary by Severity:")
    report.append(f"  CRITICAL: {critical}")
    report.append(f"  HIGH: {high}")
    report.append(f"  MEDIUM: {medium}")
    report.append(f"  LOW: {low}")
    
    # Detailed findings
    report.append("\n" + "=" * 70)
    report.append("DETAILED FINDINGS")
    report.append("=" * 70)
    
    if not vulnerabilities:
        report.append("\n[✓] No known vulnerabilities detected on open ports!")
        report.append("Note: Absence of known vulnerabilities doesn't mean the system is secure.")
    else:
        for vuln in vulnerabilities:
            report.append(f"\n[Port {vuln['port']}] {vuln['service']}")
            report.append(f"  Severity: {vuln['severity']}")
            report.append(f"  Issue: {vuln['vulnerability']}")
            if vuln['banner']:
                report.append(f"  Banner: {vuln['banner']}")
    
    # Open ports list
    report.append("\n" + "=" * 70)
    report.append(f"OPEN PORTS ({len(scan_results['open'])})")
    report.append("=" * 70)
    
    if scan_results['open']:
        for port in sorted(scan_results['open']):
            service = VULNERABLE_PORTS.get(port, {}).get('service', 'Unknown')
            report.append(f"  Port {port}: {service}")
    else:
        report.append("  No open ports found!")
    
    # Recommendations
    report.append("\n" + "=" * 70)
    report.append("SECURITY RECOMMENDATIONS")
    report.append("=" * 70)
    report.append("""
1. FIREWALL CONFIGURATION
   - Close unnecessary ports using firewall rules
   - Only expose ports that are absolutely required
   - Use IP whitelist if possible

2. SERVICE UPDATES
   - Keep all services and applications up to date
   - Apply security patches promptly
   - Remove unused services

3. ENCRYPTION
   - Use HTTPS instead of HTTP
   - Use SSH instead of Telnet
   - Enable TLS/SSL for all services

4. AUTHENTICATION
   - Enforce strong passwords (min 12 characters)
   - Enable multi-factor authentication (MFA)
   - Disable default credentials

5. MONITORING
   - Monitor port activity and logs regularly
   - Set up alerts for suspicious connections
   - Use intrusion detection systems (IDS)

6. ACCESS CONTROL
   - Restrict access to sensitive ports (DB, RDP, SSH)
   - Use VPNs for remote access
   - Implement network segmentation
    """)
    
    report.append("\n" + "=" * 70)
    report.append("END OF REPORT")
    report.append("=" * 70)
    
    return "\n".join(report)


def save_report(report: str, filename: str = None):
    """
    Save vulnerability report to a file
    
    Args:
        report: Report text content
        filename: Output filename (auto-generated if not provided)
    """
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"vulnerability_report_{timestamp}.txt"
    
    try:
        with open(filename, 'w') as f:
            f.write(report)
        print_colored(f"\n[✓] Report saved to: {filename}", Colors.GREEN)
        return filename
    except IOError as e:
        print_colored(f"[ERROR] Could not save report: {e}", Colors.RED)
        return None


def main():
    """Main function to run the vulnerability scanner"""
    
    print_header()
    
    # Get target from user
    print_colored("Enter target IP address or hostname (or 'localhost' to scan local machine):", Colors.CYAN)
    target = input(f"{Colors.BOLD}>>> {Colors.RESET}").strip()
    
    if not target:
        print_colored("[ERROR] No target provided!", Colors.RED)
        sys.exit(1)
    
    # Resolve hostname to IP if needed
    print_colored(f"\n[*] Resolving target address...", Colors.BLUE)
    
    if target.lower() == 'localhost':
        ip_address = "127.0.0.1"
        print_colored(f"[✓] Target: localhost (127.0.0.1)", Colors.GREEN)
    else:
        ip_address = resolve_hostname(target)
        if ip_address:
            print_colored(f"[✓] Target: {target} ({ip_address})", Colors.GREEN)
        else:
            print_colored(f"[ERROR] Could not resolve: {target}", Colors.RED)
            sys.exit(1)
    
    # Ask which ports to scan
    print_colored(f"\nSelect scan range:", Colors.CYAN)
    print_colored("1. Quick scan (common ports: 21-23, 80, 443, 3306, 3389, 5432)", Colors.WHITE)
    print_colored("2. Standard scan (ports 1-1024)", Colors.WHITE)
    print_colored("3. Full scan (ports 1-65535 - may take long!)", Colors.WHITE)
    print_colored("4. Custom port range", Colors.WHITE)
    
    choice = input(f"{Colors.BOLD}>>> {Colors.RESET}").strip()
    
    if choice == '1':
        ports_to_scan = [21, 22, 23, 80, 443, 3306, 3389, 5432, 8080, 27017]
    elif choice == '2':
        ports_to_scan = list(range(1, 1025))
    elif choice == '3':
        ports_to_scan = list(range(1, 65536))
    elif choice == '4':
        print_colored("Enter port range (e.g., '80-443' or '80,443,3306'):", Colors.CYAN)
        port_input = input(f"{Colors.BOLD}>>> {Colors.RESET}").strip()
        try:
            if '-' in port_input:
                start, end = port_input.split('-')
                ports_to_scan = list(range(int(start), int(end) + 1))
            else:
                ports_to_scan = [int(p.strip()) for p in port_input.split(',')]
        except ValueError:
            print_colored("[ERROR] Invalid port format!", Colors.RED)
            sys.exit(1)
    else:
        print_colored("[ERROR] Invalid choice!", Colors.RED)
        sys.exit(1)
    
    # Run the scan
    start_time = time.time()
    scan_results = scan_port_range(ip_address, ports_to_scan)
    scan_time = time.time() - start_time
    
    # Analyze vulnerabilities
    vulnerabilities = analyze_vulnerabilities(ip_address, scan_results['open'])
    
    # Generate report
    report = generate_report(target, target, scan_results, vulnerabilities, scan_time)
    
    # Display and save report
    print_colored("\n" + report, Colors.WHITE)
    save_report(report)
    
    print_colored("\n[*] Scan completed successfully!", Colors.GREEN)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_colored("\n\n[!] Scan interrupted by user", Colors.YELLOW)
        sys.exit(0)
    except Exception as e:
        print_colored(f"\n[ERROR] Unexpected error: {e}", Colors.RED)
        sys.exit(1)
