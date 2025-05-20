#!/bin/bash

echo "[*] إعداد البيئة..."

apt update && apt upgrade -y || true
pkg install python git termux-api || true
pip install requests flask pyinstaller pyautogui opencv-python keyboard

mkdir -p /var/www/html/rat

echo "[+] البيئة جاهزة!"