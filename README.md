# Task 0: Python Fundamentals, Data Analysis & Git

**Author:** Aditya Kumar Nag  
**Repository:** [task-0](https://github.com/AdityaKrNag007/task-0)

---

## Overview
This repository contains the complete solutions for **Task 0**, covering core Python fundamentals, list operations, functions, control flow (`for-else`), array operations with **NumPy**, tabular data processing with **Pandas**, and data visualization using **Matplotlib**[cite: 2].

---

## Repository Structure

```text
task-0/
├── README.md
├── requirements.txt
├── .gitignore
├── q1.py
├── q2.py
├── q3.py
├── q4.py
├── q5.py
├── q6.py
├── data/
│   ├── student_performance.csv
│   └── processed_student_performance.csv
└── plots/
    ├── final_scores.png
    ├── study_vs_score.png
    ├── score_distribution.png
    └── custom_plot.png
```

---

## Requirements & Installation

This project requires **Python 3.8+** and the following libraries[cite: 2]:
* `numpy`[cite: 2]
* `pandas`[cite: 2]
* `matplotlib`[cite: 2]

Install dependencies via `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## Commands to Run the Solutions

Execute each script from the root `task-0` directory:

### Question 1: List Analyzer
Reads an integer $N$ followed by space-separated integers to compute statistics manually without built-in functions[cite: 2].
```bash
python q1.py
```
*Example input:*
```text
6
4 7 2 9 6 3
```

### Question 2: Lists, Functions and `.copy()`
Runs the function demonstrating non-destructive list manipulation, filtering negative numbers, and sorting[cite: 2].
```bash
python q2.py
```

### Question 3: Prime Numbers Using `for-else`
Checks for primes using Python's `for-else` syntax and prints all primes up to $N$[cite: 2].
```bash
python q3.py
```
*Example input:*
```text
20
```

### Question 4: NumPy Basics
Performs vectorized calculations, statistical summaries, bonus marks additions, and boolean indexing[cite: 2].
```bash
python q4.py
```

### Question 5: Pandas and CSV Analysis
Loads `data/student_performance.csv`, computes score and attendance metrics, and exports `data/processed_student_performance.csv`[cite: 1, 2].
```bash
python q5.py
```

### Question 6: Visualizing Data with Matplotlib
Processes the dataset and saves all 4 plot images into the `plots/` folder[cite: 1, 2].
```bash
python q6.py
```