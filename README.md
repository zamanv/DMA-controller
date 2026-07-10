# DMA controller
# Direct Memory Access (DMA) Controller

A simulation of a **Direct Memory Access (DMA) Controller** demonstrating high-speed data transfer between memory and I/O devices with minimal CPU intervention. This project implements and compares **Burst Mode** and **Cycle Stealing Mode** using **Logisim** and **Python**.

## Overview

Direct Memory Access (DMA) allows data to be transferred directly between memory and I/O devices without requiring continuous CPU involvement. This improves system performance by reducing CPU workload and increasing data transfer efficiency.

This project includes:
- Hardware-level DMA design using **Logisim**
- Software simulation using **Python**
- Comparison of **Burst Mode** and **Cycle Stealing Mode**
- Bus arbitration using **Bus Request (BR)** and **Bus Grant (BG)** signals

---

## Features

- DMA Controller simulation
- Burst Mode implementation
- Cycle Stealing Mode implementation
- Bus Request (BR) and Bus Grant (BG) handshake
- Logisim hardware simulation
- Python GUI-based simulation
- Thread-based DMA simulation
- Performance comparison between DMA modes

---

## Technologies Used

- Logisim Evolution
- Python 3
- Tkinter (GUI)
- Matplotlib (Performance Graphs)
- Threading

---

## DMA Transfer Modes

### Burst Mode
- DMA takes full control of the system bus.
- Transfers an entire block of data continuously.
- Highest transfer speed.
- CPU remains paused until transfer completes.

### Cycle Stealing Mode
- DMA transfers one word at a time.
- CPU regains bus access between transfers.
- Better CPU responsiveness.
- Slightly slower than Burst Mode.

---

## Bus Arbitration

The DMA controller communicates with the CPU using:

- **BR (Bus Request):** DMA requests control of the system bus.
- **BG (Bus Grant):** CPU grants bus access to the DMA controller.

This handshake ensures safe and conflict-free data transfers.

---

## Project Structure

```
DMA-Controller/
│
├── Logisim/
│   ├── Burst_Mode.circ
│   └── Cycle_Stealing.circ
│
├── Python/
│   ├── dma_gui.py
│   ├── dma_thread.py
│   └── requirements.txt
│
│
├── Report_DMA.pdf
└── README.md
```

---

## Results

| Feature | Burst Mode | Cycle Stealing |
|----------|------------|----------------|
| Transfer Speed | Fast | Moderate |
| CPU Availability | No | Yes |
| Bus Control | Continuous | One Cycle at a Time |
| Throughput | High | Medium |

The simulations demonstrate:

- Reduced CPU workload
- Efficient bus utilization
- Successful memory-to-I/O data transfers
- Correct BR/BG handshake operation

---

## Learning Outcomes

- Understanding DMA architecture
- Bus arbitration techniques
- Logisim-based digital circuit design
- Python-based hardware simulation
- Performance comparison of DMA transfer modes

---

## Future Improvements

- Multi-channel DMA support
- Priority-based bus arbitration
- Scatter-Gather DMA
- Interrupt-driven DMA completion
- Integration with processor simulation

---

## References

- William Stallings – *Computer Organization and Architecture*
- David A. Patterson & John L. Hennessy – *Computer Organization and Design*
- Logisim Evolution
- GeeksforGeeks – Direct Memory Access (DMA)

---

## Author

**Adil Zaman V**

Government Engineering College, Idukki

Department of Computer Science & Engineering

Course: Computer Organization and Architecture
