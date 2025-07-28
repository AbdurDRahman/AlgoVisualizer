# Algo Visualizer

Algo Visualizer is a Python-based tool to visualize common sorting algorithms step-by-step. Built using Pygame, this project helps users understand how sorting algorithms work internally through animated visuals.

## Features

- Visualizes popular sorting algorithms:
  - Bubble Sort
  - Insertion Sort
  - Merge Sort
  - Quick Sort
- Step-by-step transitions for comparisons and swaps
- Interactive GUI menu for algorithm selection
- Designed for learning and demonstration purposes

##  How It Works

Each sorting algorithm is implemented as a **generator function**, yielding control after each important operation like a comparison or swap. This lets the main event loop draw and update the list dynamically.

## 🖥️ Technologies Used

- Python 3
- Pygame

## 📂 Project Structure
 .
├──  functions.py
├──  main.py
├──  mergeSort.py
├──  pyproject.toml
├──  README.md
├──  UI
│   ├──  button.py
│   ├──  draw_down_menu.py
│   ├──  list_display.py
│   ├──  menu.py
│   └──  UIconstants.py
├──  uv.lock
└──  visualizer
    └──  sorting
        ├──  bubbleSort.py
        ├──  insertionSort.py
        ├──  mergeSort.py
        ├──  quickSort.py
        └──  selectionSort.py
---

## 🔧 Setup & Run

### Recommended: Using [uv](https://github.com/astral-sh/uv)

1. **Install uv**
   ```bash
   curl -Ls https://astral.sh/uv/install.sh | sh
Clone the repo

bash
Copy
Edit
git clone https://github.com/AbdurDRahman/AlgoVisualizer.git
cd AlgoVisualizer
Install dependencies

bash
Copy
Edit
uv pip install -r requirements.txt
Run the app

bash
Copy
Edit
python main.py