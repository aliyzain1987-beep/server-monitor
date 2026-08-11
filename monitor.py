import socket
import getpass
import platform
from datetime import datetime
import psutil
import os


# 1. Hostname
hostname = socket.gethostname()

# 2. Current User
current_user = getpass.getuser()

# 3. Date and Time
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
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    sock.connect(("8.8.8.8", 80))
    ip_address = sock.getsockname()[0]
except OSError:
    ip_address = "Unable to determine IP"
finally:
    sock.close()

# 10. System Uptime
boot_time = datetime.fromtimestamp(psutil.boot_time())
uptime_delta = datetime.now() - boot_time

days = uptime_delta.days
hours = uptime_delta.seconds // 3600
minutes = (uptime_delta.seconds % 3600) // 60

uptime = f"{days} Days {hours} Hours {minutes} Minutes"


# Create Server Health Report
report = f"""
=============================
SERVER HEALTH REPORT
=============================

Hostname         : {hostname}
Current User     : {current_user}
Date             : {current_time}
Operating System : {operating_system}
Kernel           : {kernel_version}
CPU Usage        : {cpu_usage}%

Memory Usage
Total            : {total_ram:.2f} GB
Used             : {used_ram:.2f} GB
Free             : {free_ram:.2f} GB
Usage            : {memory_percent}%

Disk Usage
Filesystem       : /
Used             : {disk_used:.2f} GB
Available        : {disk_free:.2f} GB
Usage            : {disk_percent}%

IP Address       : {ip_address}
Uptime           : {uptime}
"""


# Display report
print(report)


# Generate reports/server_report.txt
os.makedirs("reports", exist_ok=True)

report_file = "reports/server_report.txt"

with open(report_file, "w") as file:
    file.write(report)

print(f"Report saved to: {report_file}")
