# ReconXploit (Automated Machines Hacking Tool)

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
   git clone https://github.com/4rti7t/ReconXploit.git
   cd ReconXploit
   ```
   
   ![Screenshot from 2024-11-23 18-27-19](https://github.com/user-attachments/assets/6c955800-3d87-4751-ad0d-5bb77ffb6590)

2. Install the required Python modules:
   ```bash
   pip install -r requirements.txt
   ```

   ![Screenshot from 2024-11-23 18-33-45](https://github.com/user-attachments/assets/18ffea76-efe8-403f-bfa9-10c81c4544a6)


3. Ensure the necessary tools (Nmap, Nikto, Gobuster, etc.) are installed and accessible from your terminal.

---

## 🛠️ Usage
1. Run the script:
   ```bash
   python3 ReconXploit.py
   ```
![Screenshot from 2024-11-23 18-36-29](https://github.com/user-attachments/assets/8b5b600f-5c8b-4f76-aa47-cf9a31083913)

   

2. Follow the menu options to:
   - 🔍 Scan a target.
   - 🛠️ Enumerate services.
   - 📂 Search for vulnerabilities.
   - 💥 Exploit the target.
   - 📊 Perform post-exploitation tasks.

---

## 📖 **Menu Options:**
![Screenshot from 2024-11-23 18-36-55](https://github.com/user-attachments/assets/77c425d1-041d-4b86-91d6-ae86d3f3fb81)


1. **Scan Target**:
    Perform a network scan on the specified IP to identify open ports and services.
   

3. **Enumerate Services**:
   Use tools like Nikto and Gobuster to gather additional information.
   

5. **Search for Vulnerabilities**:
   Search for known vulnerabilities using Searchsploit.
   
7. **Exploit Target**:
    Exploit discovered vulnerabilities using Metasploit.
   

9. **Post-Exploitation**:
    Collect system details and resource usage for further analysis.
   

11. **Exit**:
    Exit the program.

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

For any issues, feel free to open an issue on GitHub or contact us at arti7tofficial@gmail.com.

---


Happy Ethical Hacking! 🚀

