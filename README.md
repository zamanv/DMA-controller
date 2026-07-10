# 🚀 Direct Memory Access (DMA) Controller

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Logisim](https://img.shields.io/badge/Logisim-Evolution-green?style=for-the-badge)
![Architecture](https://img.shields.io/badge/Computer-Architecture-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)

</p>

<p align="center">
A hardware and software simulation of a <b>Direct Memory Access (DMA) Controller</b> demonstrating efficient memory-I/O data transfers using <b>Logisim</b> and <b>Python</b>.
</p>

---

# 📖 Overview

Modern computer systems rely on **Direct Memory Access (DMA)** to move data between memory and I/O devices without continuously involving the CPU.

This project demonstrates how DMA improves:

- ⚡ Data transfer speed
- 🧠 CPU utilization
- 🚌 Bus efficiency
- 📈 Overall system performance

Both **Burst Mode** and **Cycle Stealing Mode** are implemented and compared using hardware and software simulations.

---

# ✨ Features

✅ Logisim DMA Controller

✅ Burst Mode

✅ Cycle Stealing Mode

✅ BR/BG Bus Arbitration

✅ Python GUI Simulation

✅ Thread-based DMA Simulation

✅ Performance Comparison

✅ Memory Transfer Visualization

---

# 🏗️ Project Architecture

```text
              +----------------+
              |      CPU       |
              +-------+--------+
                      |
                 Bus Request
                      |
                      ▼
          +----------------------+
          |    DMA Controller    |
          +----------+-----------+
                     |
             Bus Grant / Control
                     |
      +--------------+--------------+
      |                             |
      ▼                             ▼
+-------------+              +--------------+
| I/O Device  |────────────▶ | Main Memory  |
+-------------+              +--------------+
```

---

# 🔄 DMA Modes

| 🚀 Burst Mode | 🔄 Cycle Stealing |
|---------------|------------------|
| Highest speed | CPU remains responsive |
| CPU paused | CPU executes between transfers |
| Continuous bus access | Bus shared every cycle |

---

# 📊 Performance

| Feature | Burst | Cycle Stealing |
|---------|-------|----------------|
| Transfer Speed | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| CPU Availability | ❌ | ✅ |
| Bus Utilization | High | Moderate |
| Throughput | High | Medium |

---

# 📷 Screenshots

## Logisim Circuit

> Add your screenshot here

```md
![Burst Mode](images/burst_mode.png)
```

---

## Cycle Stealing

```md
![Cycle Stealing](images/cycle_stealing.png)
```

---

## Python GUI

```md
![GUI](images/gui.png)
```

---

## Performance Graph

```md
![Performance](images/performance_graph.png)
```

---

# ⚙️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Software Simulation |
| Tkinter | GUI |
| Threading | Parallel Execution |
| Matplotlib | Performance Graph |
| Logisim Evolution | Hardware Design |

---

# 📂 Project Structure

```text
DMA-Controller
│
├── Logisim
│   ├── Burst_Mode.circ
│   └── Cycle_Stealing.circ
│
├── Python
│   ├── dma_gui.py
│   ├── dma_thread.py
│
├── images
│
├── Report_DMA.pdf
│
└── README.md
```

---

# 🚀 Getting Started

Clone the repository

```bash
git clone https://github.com/zamanv/DMA-controller.git
```

Move into the project

```bash
cd DMA-controller
```

Run the Python simulation

```bash
python dma_gui.py
```

---

# 🎯 Learning Outcomes

- Computer Organization
- DMA Architecture
- Bus Arbitration
- Memory Systems
- Hardware Simulation
- Python GUI Programming
- Performance Analysis

---

# 🔮 Future Improvements

- Multi-channel DMA

- Scatter-Gather DMA

- Interrupt-driven DMA

- Priority Bus Arbitration

- Cache Coherency Support

---

# 📚 References

- Computer Organization and Architecture — William Stallings

- Computer Organization and Design — Patterson & Hennessy

- Logisim Evolution

---

# 👨‍💻 Author

## Adil Zaman V

🎓 Government Engineering College, Idukki

Department of Computer Science & Engineering

---

<p align="center">

⭐ If you found this project useful, consider giving it a star!

</p>
