import time
import threading

class MainMemory:
    """Simulates the physical RAM of the computer."""
    def __init__(self, size=256):
        # Initialize memory with zeros
        self.data = [0] * size

class DMAController(threading.Thread):
    """
    Simulates the actual DMA hardware chip. 
    It runs in its own thread so it can operate simultaneously with the CPU.
    """
    def __init__(self, memory):
        super().__init__()
        self.memory = memory
        self.daemon = True  # Allows the program to exit when the CPU finishes
        
        # Simulated Memory-Mapped Registers
        self.source_addr = 0
        self.dest_addr = 0
        self.length = 0
        self.status = "IDLE"
        
        # Internal hardware trigger
        self._start_signal = threading.Event()

    def configure(self, src, dest, length):
        """CPU calls this to set up the transfer."""
        self.source_addr = src
        self.dest_addr = dest
        self.length = length

    def trigger(self):
        """CPU calls this to flip the 'START' switch."""
        self.status = "BUSY"
        self._start_signal.set()

    def run(self):
        """This is the infinite loop running inside the DMA hardware."""
        while True:
            # The DMA sleeps until the CPU triggers it
            self._start_signal.wait()
            self._start_signal.clear()
            
            print(f"\n[DMA Hardware] -> Taking control of the bus.")
            print(f"[DMA Hardware] -> Moving {self.length} words from {self.source_addr} to {self.dest_addr}...\n")
            
            # Perform the actual memory transfer
            for i in range(self.length):
                # We add a small sleep to simulate the time it takes to move data over a bus
                time.sleep(0.2) 
                
                # Copy data from source to destination
                src_index = self.source_addr + i
                dest_index = self.dest_addr + i
                self.memory.data[dest_index] = self.memory.data[src_index]
                
            print("\n[DMA Hardware] -> Transfer Complete! Sending Interrupt to CPU...\n")
            self.status = "IDLE"

def cpu_execution():
    """Simulates the main program running on the CPU."""
    ram = MainMemory()
    dma = DMAController(ram)
    dma.start() # Power on the DMA hardware (starts the background thread)

    # 1. CPU puts some test data into RAM
    ram.data[10] = 99
    ram.data[11] = 88
    ram.data[12] = 77
    print(f"[CPU] Initial Source Data (Addr 10-12): {ram.data[10:13]}")
    print(f"[CPU] Initial Dest Data   (Addr 50-52): {ram.data[50:53]}\n")

    # 2. CPU configures the DMA
    print("[CPU] Setting up DMA registers...")
    dma.configure(src=10, dest=50, length=3)
    
    # 3. CPU starts the DMA
    print("[CPU] Triggering DMA and moving on to other tasks!\n")
    dma.trigger()

    # 4. CPU does its own work while DMA copies data in the background
    for step in range(1, 6):
        print(f"[CPU] Calculating complex mathematics... (Step {step})")
        time.sleep(0.15) # The CPU works at its own pace

    # 5. CPU needs the copied data, so it checks if DMA is done
    print("\n[CPU] I need the new data. Checking DMA status...")
    while dma.status == "BUSY":
        print("[CPU] DMA is still busy. Waiting...")
        time.sleep(0.1)

    print("[CPU] DMA is idle. Reading destination memory!")
    print(f"[CPU] Final Source Data (Addr 10-12): {ram.data[10:13]}")
    print(f"[CPU] Final Dest Data   (Addr 50-52): {ram.data[50:53]}")

if __name__ == "__main__":
    cpu_execution()