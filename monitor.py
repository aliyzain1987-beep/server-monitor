import socket
import getpass
import platform
from datetime import datetime
import psutil

# 1. Hostname
hostname = socket.gethostname()

# 2. Current logged-in user
current_user = getpass.getuser()

# 3. Current date and time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

# 4. Operating System
operating_system = platform.platform()

# 5. Kernel Version
kernel_version = platform.release()

# 6. CPU Usage
cpu_usage = psutil.cpu_percent(interval=1)

# 7. Memory Usage
memory = psutil.virtual_memory()

total_ram = memory.total / (1024 ** 3)
used_ram = memory.used / (1024 ** 3)
free_ram = memory.available / (1024 ** 3)
memory_percent = memory.percent

# 8. Disk Usage
disk = psutil.disk_usage("/")

disk_used = disk.used / (1024 ** 3)
disk_free = disk.free / (1024 ** 3)
disk_percent = disk.percent

# 9. Primary IPv4 Address
hostname_ip = socket.gethostname()
ip_address = socket.gethostbyname(hostname_ip)


# Display Results

print("\n===== SERVER MONITOR =====\n")

print(f"Hostname       : {hostname}")
print(f"Current User   : {current_user}")
print(f"Date & Time    : {current_time}")
print(f"Operating System : {operating_system}")
print(f"Kernel Version : {kernel_version}")
print(f"CPU Usage      : {cpu_usage}%")

print("\nMemory Usage")
print(f"Total : {total_ram:.2f} GB")
print(f"Used  : {used_ram:.2f} GB")
print(f"Free  : {free_ram:.2f} GB")
print(f"Usage : {memory_percent}%")

print("\nDisk Usage")
print("Filesystem : /")
print(f"Used       : {disk_used:.2f} GB")
print(f"Available  : {disk_free:.2f} GB")
print(f"Usage      : {disk_percent}%")

print("\nNetwork")
print(f"IP Address : {ip_address}")
