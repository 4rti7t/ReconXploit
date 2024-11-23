# Automated Hacking Tool

## 🚀 Overview
The **Automated Hacking Tool** is designed to streamline the penetration testing process by automating tasks such as scanning, enumeration, vulnerability detection, exploitation, and post-exploitation. This tool is ideal for ethical hackers and cybersecurity professionals looking to enhance their workflow.

---

## 🌟 Features
- 🔍 **Target Scanning**: Detect open ports, services, and system details using Nmap.
- 🛠️ **Service Enumeration**: Discover vulnerabilities and hidden directories with Nikto and Gobuster.
- 📂 **Vulnerability Detection**: Identify exploits for services and versions using Searchsploit.
- 💥 **Exploitation Module**: Test Metasploit exploits with ease.
- 📊 **Post-Exploitation Commands**: Collect detailed system information for analysis.

---

## 📋 Prerequisites
- 🖥️ A Linux-based operating system (**Kali Linux** recommended).
- 🐍 Python 3.x installed.
- ⚙️ Required tools installed:
  - `nmap`
  - `nikto`
  - `gobuster`
  - `searchsploit`
  - `metasploit`

---

## 📥 Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/automated-hacking-tool.git
   cd automated-hacking-tool
   ```
   
   ![Clone Repository Screenshot](screenshots/clone-repo.png)

2. Install the required Python modules:
   ```bash
   pip install -r requirements.txt
   ```

   ![Install Requirements Screenshot](screenshots/install-requirements.png)

3. Ensure the necessary tools (Nmap, Nikto, Gobuster, etc.) are installed and accessible from your terminal.

---

## 🛠️ Usage
1. Run the script:
   ```bash
   python3 automated_hacking_tool.py
   ```

   ![Run Script Screenshot](screenshots/run-script.png)

2. Follow the menu options to:
   - 🔍 Scan a target.
   - 🛠️ Enumerate services.
   - 📂 Search for vulnerabilities.
   - 💥 Exploit the target.
   - 📊 Perform post-exploitation tasks.

---

## 📖 Menu Options
1. **Scan Target**: Perform a network scan on the specified IP to identify open ports and services.
   ![Scan Target Screenshot](screenshots/scan-target.png)

2. **Enumerate Services**: Use tools like Nikto and Gobuster to gather additional information.
   ![Enumerate Services Screenshot](screenshots/enumerate-services.png)

3. **Search for Vulnerabilities**: Search for known vulnerabilities using Searchsploit.
   ![Search Vulnerabilities Screenshot](screenshots/search-vulnerabilities.png)

4. **Exploit Target**: Exploit discovered vulnerabilities using Metasploit.
   ![Exploit Target Screenshot](screenshots/exploit-target.png)

5. **Post-Exploitation**: Collect system details and resource usage for further analysis.
   ![Post-Exploitation Screenshot](screenshots/post-exploitation.png)

6. **Exit**: Exit the program.

---

## ⚠️ **Disclaimer**
This tool is intended for **educational and ethical hacking purposes only**. Unauthorized use against systems without explicit permission is illegal and punishable under law. The developers are not responsible for any misuse or damage caused by this tool.

---

## 🤝 **Contributing**

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

---

## 📜 **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 📞 **Support**
For any issues, feel free to open an issue on GitHub or contact us at support@example.com.

---


Happy Ethical Hacking! 🚀

