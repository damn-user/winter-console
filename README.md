# 🎄 winter-console
***☃️ Bring 3D New Year’s spirit to your console ❄️***

A collection of lightweight, dependency-free Python scripts featuring real-time **3D rotating ASCII animations** to create a festive atmosphere right in your terminal.

## ✨ Features
* **Pure 3D Math:** Real-time 3D projection, rotation matrices, and lighting/depth rendering implemented from scratch.
* **Zero dependencies:** Built using only Python's standard library (no `numpy`, `pygame`, or `curses` required).
* **Lightweight & Fast:** Smooth terminal animation with minimal CPU/RAM usage.
* **Cross-platform:** Works out of the box on Windows, macOS, and Linux terminals.

## 📂 What's inside
* `tree.py` — A 3D spinning Christmas tree rendered in ASCII.
* `fallen_snow.py` — A 3D-like falling snow animation with depth effect.
* `tree_and_snow.py` — The ultimate holiday scene: a 3D rotating Christmas tree surrounded by falling snow.
* `ring.py` — A classic 3D spinning torus/ring animation.

## 🚀 Getting Started

### Prerequisites
Make sure you have **Python 3.x** installed. No `pip install` needed!

### Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com
   cd winter-console
   ```

2. Run any 3D animation:
   ```bash
   python tree_and_snow.py
   ```
   *(On macOS/Linux, you might need to use `python3` instead of `python`)*

3. Press `Ctrl + C` to exit.

## 📸 Preview
https://github.com/user-attachments/assets/b33ce83c-06c2-415a-8be1-b9a36f8afc2d



## 🧠 How it works
Each script calculates 3D coordinates `(x, y, z)`, applies rotation matrices over time, and projects the points onto a 2D terminal grid using ASCII characters to simulate depth and shading.
