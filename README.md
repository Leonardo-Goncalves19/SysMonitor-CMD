# SysMonitor CMD

**SysMonitor CMD** is a **real-time system monitor** for **Windows**, running entirely in the **terminal (CMD or PowerShell)**.  
It displays detailed information about **GPU, RAM, disks, and top processes**, using **Rich** for an elegant and interactive interface — **no GUI required**.

---

## 🔹 Features

- **Real-time monitoring** of CPU, RAM, and disks.  
- Displays the **top resource-consuming applications**.  
- Supports **NVIDIA GPUs** via `nvidia-smi`.  
- Colorful, interactive terminal interface powered by **Rich**.  
- Lightweight, fast, and fully **terminal-friendly**.

---

## 🔹 Prerequisites

1. **Python 3.10+**  
2. **Windows** (GPU monitoring requires `nvidia-smi`)  
3. Required Python libraries:

```bash
pip install psutil rich
