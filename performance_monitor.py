import psutil
import time

def monitor_performance():
    while True:
        memory_info = psutil.virtual_memory()
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"Memory Usage: {memory_info.percent}%")
        print(f"CPU Usage: {cpu_usage}%")
        time.sleep(5)

if __name__ == "__main__":
    monitor_performance()
