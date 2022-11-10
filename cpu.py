#check data being sent to the server
import socket
import psutil
import platform
from datetime import datetime

# get the system name
system_name = platform.node()
# get the system IP address
system_ip = socket.gethostbyname(socket.gethostname())
# get the system platform
system_platform = platform.system()
# get the system architecture
system_architecture = platform.machine()
# get the system version
system_version = platform.version()
# get the system processor
system_processor = platform.processor()
# get the system memory
system_memory = psutil.virtual_memory().total >> 20
# get the system disk space
system_disk = psutil.disk_usage('/').total >> 20
# get the system boot time
system_boot_time = datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
# get the system uptime
system_uptime = datetime.now() - datetime.fromtimestamp(psutil.boot_time())
# get the system CPU usage
system_cpu_usage = psutil.cpu_percent()
system_cpu_core = psutil.cpu_count(logical=False)
# get the system CPU thread count
system_cpu_thread = psutil.cpu_count(logical=True)

print('System name:'+system_name)
print('IP Address: ' + system_ip)
print('Platform: ' + system_platform)
print('Architecture: ' + system_architecture)
print('Version: ' + system_version)
print('Processor: ' + system_processor)
print('Memory: ' + str(system_memory) + ' MB')
print('Disk: ' + str(system_disk) + ' MB')
print('Boot Time: ' + system_boot_time)
print('Uptime: ' + str(system_uptime))
print('CPU Usage: ' + str(system_cpu_usage) + '%')