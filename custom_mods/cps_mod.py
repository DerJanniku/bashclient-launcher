
import time
import threading

class CPSMod:
    def __init__(self):
        self.cps = 0
        self.clicks = 0
        self.running = True
        self.thread = threading.Thread(target=self.calculate_cps)
        self.thread.start()

    def calculate_cps(self):
        while self.running:
            start_time = time.time()
            time.sleep(1)
            end_time = time.time()
            self.cps = self.clicks / (end_time - start_time)
            self.clicks = 0
            print(f"CPS: {self.cps:.2f}")

    def register_click(self):
        self.clicks += 1

    def stop(self):
        self.running = False
        self.thread.join()

if __name__ == "__main__":
    cps_mod = CPSMod()
    try:
        while True:
            time.sleep(0.1)
            cps_mod.register_click()  # Simulate a click
    except KeyboardInterrupt:
        cps_mod.stop()
