
import time
import threading

class FPSMod:
    def __init__(self):
        self.fps = 0
        self.running = True
        self.thread = threading.Thread(target=self.calculate_fps)
        self.thread.start()

    def calculate_fps(self):
        while self.running:
            start_time = time.time()
            time.sleep(1)
            end_time = time.time()
            self.fps = 1 / (end_time - start_time)
            print(f"FPS: {self.fps:.2f}")

    def stop(self):
        self.running = False
        self.thread.join()

if __name__ == "__main__":
    fps_mod = FPSMod()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        fps_mod.stop()
