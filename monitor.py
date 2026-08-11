import socket
import getpass
# Get system hostname
hostname = socket.gethostname()

# Get current logged-in user
current_user = getpass.getuser()

print("===== SERVER MONITOR =====")
print(f"Hostname     : {hostname}")
print(f"Current User : {current_user}")

