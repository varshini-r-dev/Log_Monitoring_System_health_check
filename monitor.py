import psutil
import datetime
import time

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

def get_disk_usage():
    disk_before = psutil.disk_io_counters()
    time.sleep(1)
    disk_after = psutil.disk_io_counters()
    
    read_bytes = disk_after.read_bytes - disk_before.read_bytes
    write_bytes = disk_after.write_bytes - disk_before.write_bytes
    
    read_mb = round(read_bytes / 1024 / 1024, 2)
    write_mb = round(write_bytes / 1024 / 1024, 2)
    
    return read_mb, write_mb

def display_stats():
    print("="*40)
    print(f"System Health Check - {datetime.datetime.now()}")
    print("="*40)       
    print(f"CPU Usage: {get_cpu_usage()}%")
    print(f"Memory Usage: {get_memory_usage()}%")           
    read_mb, write_mb = get_disk_usage()
    print(f"Disk Read Speed  : {read_mb} MB/s")
    print(f"Disk Write Speed : {write_mb} MB/s")
    
display_stats()
