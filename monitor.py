import psutil
import datetime
import time
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "system_health.log")
os.makedirs(LOG_DIR, exist_ok=True)

ALERT_THRESHOLD = 70

def get_stats():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return cpu, memory, disk

def check_alerts(cpu, memory, disk):
    alerts = []
    if cpu > ALERT_THRESHOLD:
        alerts.append(f"[ALERT] CPU is HIGH: {cpu}%")
    if memory > ALERT_THRESHOLD:
        alerts.append(f"[ALERT] Memory is HIGH: {memory}%")
    if disk > ALERT_THRESHOLD:
        alerts.append(f"[ALERT] Disk is HIGH: {disk}%")
    return alerts

def log_and_display():
    cpu, memory, disk = get_stats()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    log_line = f"{timestamp} | CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%"
    
    print("="*50)
    print(log_line)
    
    alerts = check_alerts(cpu, memory, disk)
    for alert in alerts:
        print(alert)
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_line + "\n")
        for alert in alerts:
            f.write(alert + "\n")

print("Monitoring started... Press Ctrl+C to stop")
while True:
    log_and_display()
    time.sleep(60)