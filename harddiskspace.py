#get hard disk space usage in percent
import shutil
import psutil
def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["","K","M","G","T","P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def get_disk_space():
    print("="*40, "Disk Space Info", "="*40)
    print("Total: %20s GB" % get_size(shutil.disk_usage("/").total))
    print("Used: %20s GB" % get_size(shutil.disk_usage("/").used))
    print("Free: %20s GB" % get_size(shutil.disk_usage("/").free))
    print("="*80)

def get_memory_info():
    print("="*40, "Memory Info", "="*40)
    # get the memory details
    svmem = psutil.virtual_memory()
    print(f"Total: {get_size(svmem.total)}")
    print(f"Available: {get_size(svmem.available)}")
    print(f"Used: {get_size(svmem.used)}")
    print(f"Percentage: {svmem.percent}%")
    print("="*80)

if __name__ == '__main__':
    get_disk_space()
    get_memory_info()