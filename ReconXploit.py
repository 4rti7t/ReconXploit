import subprocess
import nmap
import sys
import os

# Clear screen function
def clear_screen():
    # For Windows
    if sys.platform == "win32":
        os.system('cls')
    # For Linux and macOS
    else:
        os.system('clear')

# Call the function to clear the screen
clear_screen()

# Rest of your script goes here
    

# ----- Logo and Header -----
def print_header():
    logo = """
    
   ▄████████    ▄████████  ▄████████  ▄██████▄  ███▄▄▄▄   ▀████    ▐████▀    ▄███████▄  ▄█        ▄██████▄   ▄█      ███     
  ███    ███   ███    ███ ███    ███ ███    ███ ███▀▀▀██▄   ███▌   ████▀    ███    ███ ███       ███    ███ ███  ▀█████████▄ 
  ███    ███   ███    █▀  ███    █▀  ███    ███ ███   ███    ███  ▐███      ███    ███ ███       ███    ███ ███▌    ▀███▀▀██ 
 ▄███▄▄▄▄██▀  ▄███▄▄▄     ███        ███    ███ ███   ███    ▀███▄███▀      ███    ███ ███       ███    ███ ███▌     ███   ▀ 
▀▀███▀▀▀▀▀   ▀▀███▀▀▀     ███        ███    ███ ███   ███    ████▀██▄     ▀█████████▀  ███       ███    ███ ███▌     ███     
▀███████████   ███    █▄  ███    █▄  ███    ███ ███   ███   ▐███  ▀███      ███        ███       ███    ███ ███      ███     
  ███    ███   ███    ███ ███    ███ ███    ███ ███   ███  ▄███     ███▄    ███        ███▌    ▄ ███    ███ ███      ███     
  ███    ███   ██████████ ████████▀   ▀██████▀   ▀█   █▀  ████       ███▄  ▄████▀      █████▄▄██  ▀██████▀  █▀      ▄████▀   
  ███    ███                                                                           ▀                                     
                                       \033[1mразработано @ARTIST для INFLUXION\033[0m
    """
    print(logo)
    print("Welcome to the Automated Pentest Framework!\n")
    print("Note: This tool is for educational purposes only. Unauthorized use is prohibited.\n")

# ----- Scanning Module -----
def scan_target(ip):
    nm = nmap.PortScanner()
    try:
        # Scan the first 1024 ports (you can modify the port range if needed)
        nm.scan(ip, '1-1024')

        # Check if the IP is found in the scan results
        if ip in nm.all_hosts():
            scan_result = nm[ip]

            # Format the output vertically for better readability
            result = f"Target IP: {ip}\n"
            result += f"Status: {scan_result['status']['state']} (Reason: {scan_result['status']['reason']})\n"
            result += f"MAC Address: {scan_result['addresses'].get('mac', 'N/A')}\n"
            result += f"Vendor: {scan_result['vendor'].get(scan_result['addresses'].get('mac', ''), 'N/A')}\n"
            result += "\nPorts:\n"

            for port in scan_result['tcp']:
                port_info = scan_result['tcp'][port]
                result += f"  Port {port}: {port_info['state']} (Service: {port_info['name']})\n"
                result += f"    Product: {port_info['product']}\n"
                result += f"    Version: {port_info['version']}\n"
                result += f"    Extra Info: {port_info.get('extrainfo', 'N/A')}\n"
                result += f"    CPE: {port_info['cpe']}\n"
                result += "\n"

            return result

        else:
            return f"Target {ip} not found in scan results. It might be unreachable or have no open ports."
    
    except KeyError:
        return f"Error: No results for target IP {ip}. Check if the target is reachable."
    except Exception as e:
        return f"Error occurred during scan: {str(e)}"


# ----- Enumeration Module -----
def run_nikto(target_ip):
    result = subprocess.run(['nikto', '-h', target_ip], capture_output=True, text=True)
    return result.stdout


def run_gobuster(target_ip, target_port):
    result = subprocess.run(['gobuster', 'dir', '-u', f'http://{target_ip}:{target_port}', '-w', '/usr/share/wordlists/dirb/common.txt'], capture_output=True, text=True)
    return result.stdout


# ----- Vulnerability Detection Module -----
def search_exploits(service, version):
    result = subprocess.run(['searchsploit', f'{service} {version}'], capture_output=True, text=True)
    return result.stdout


# ----- Exploitation Module -----
def exploit_target(target_ip, target_port):
    try:
        # Specify the payload and listener IP/Port
        

        # Construct the Metasploit command for the exploit
        msf_command = f"msfconsole -q -x"

        # Print the command for debugging
        print(f"Running Metasploit command: {msf_command}")

        # Run the Metasploit command and capture the output
        result = subprocess.run(msf_command, shell=True, capture_output=True, text=True)

        # Print stdout and stderr to debug
        print("Metasploit output:", result.stdout)
        print("Metasploit errors:", result.stderr)

        # Return the output
        return result.stdout

    except Exception as e:
        return f"Error occurred during exploitation: {str(e)}"




# ----- Post-Exploitation Module -----
def post_exploit(target_ip):
    print("\nGetting System Information:\n")

    # Linux Post Exploitation Commands with Emojis (for display only)
    linux_commands = [
        "=> uname        (Current Kernel ka name dakhne k ley)",
        "=>  uname -a    (Complete system info including kernel, OS, and architecture)",
        "=>  hostnamectl (OS version, kernel, hostname dakhne k ley)",
        "=>  neofetch    (Information about OS version, kernel, CPU, GPU, aur RAM usage)",
        "=>  finger john (Information about john user real name, login status, aur last login time)",
        "=>  uptime      (System ko chalaye huye kitna time ho gaya hai, aur current load dekhne k liye)",
        "=>  top         (Real-time system processes aur resource usage dekhne k liye)",
        "=>  arch        (System k architecture ka type pata chalega, jaise 64-bit (x86_64) ya 32-bit (i686))",
        "=>  lscpu       (CPU ki detailed information dekhne k liye)",
        "=>  lsblk       (Block devices (like hard drives, partitions) ki details dekhne k liye)",
        "=>  lsipc       (Info about message queues, shared memory segments, aur semaphores ki list aur unki details)",
        "=>  lspci       (System k PCI devices dekhne k liye)",
        "=>  lsusb       (System k USB devices ko list karne k liye)",
        "=>  who         (Currently logged-in users ki details dekhne k liye)",
        "=>  last        (System k last login sessions dekhne k liye)",
        "=>  df          (Disk usage ka summary dekhne k liye)",
        "=>  df -h       (Human-readable format)",
        "=>  du          (Specific directory ya file ka disk usage dekhne k liye)",
        "=>  free        (System ke RAM aur swap memory ka usage dekhne k liye)",
        "=>  free -h     (Human-readable format)",
        "=>  vmstat      (CPU, memory, disk I/O aur system processes ka real-time stats dekhne k liye)",
        "=>  vmstat 2    (Every 2 seconds stats update)",
        "=>  lsb_release (Operating system ka version aur distribution details dekhne k liye)",
        "=>  lsb_release -a",
        "=>  dmesg       (System k boot time messages ya kernel logs dekhne k liye)",
        "=>  inxi        (Detailed system information)",
        "=>  htop        (Interactive, real-time process viewer)"
        "=>  dmesg | less (Scroll through logs)",
        "=>  cat /proc/cpuinfo (CPU ke detailed specs dekhne k liye)",
        "=>  cat /proc/meminfo (Memory ka detailed stats dekhne k liye)",
    ]

    # Display Linux Commands with Emojis (only for information display)
    print("\nLinux Post-Exploitation Commands:")
    for command in linux_commands:
        print(command)

    # Linux Post Exploitation Commands (actual commands to execute)
    linux_actual_commands = [
        "uname",
        
        
    ]

    # Now execute the actual commands
    print("\nExecuting system commands...")
    for command in linux_actual_commands:
        print(f"\nExecuting: {command}")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(result.stdout)  # Display command output
        else:
            print(f"Error executing {command}: {result.stderr}")  # Display error if command fails

    print("\nPost-Exploitation information gathering completed!")

# ----- Menu Function -----
def print_menu():
    print("\n[1] Scan Target")
    print("[2] Enumerate Services")
    print("[3] Search for Vulnerabilities")
    print("[4] Exploit Target")
    print("[5] Post-Exploitation")
    print("[6] Exit")

# ----- Main Function -----
def main():
    print_header()
    target_ip = input("Enter the target IP: ")

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            print("\nScanning target...")
            print(scan_target(target_ip))

        elif choice == "2":
            print("\nEnumerating services...")
            print(run_nikto(target_ip))
            print(run_gobuster(target_ip, 80))

        elif choice == "3":
            service = input("\nEnter service (e.g., Apache): ")
            version = input("Enter version (e.g., 2.4.49): ")
            print("\nSearching for vulnerabilities...")
            print(search_exploits(service, version))

        elif choice == "4":
            print("\nExploiting target...")
            print(exploit_target(target_ip, 80))

        elif choice == "5":
            print("\nPost-Exploitation...")
            post_exploit(target_ip)

        elif choice == "6":
            print("\nExiting... Goodbye!")
            sys.exit(0)

        else:
            print("\nInvalid option! Please choose again.")

# ----- Script Entry Point -----
if __name__ == "__main__":
    main()
