# RageSort

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![Java](https://img.shields.io/badge/Java-11+-orange.svg)](https://openjdk.org/)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)]()

An adaptive Radix Sort implementation optimized by bit-length grouping for signed integers.

---

## 🛠 Complexity Analysis

### Time Complexity: $O(N \cdot \frac{K}{R})$
- **$N$**: Number of elements.
- **$K$**: Maximum bit-length of the numbers in the dataset.
- **$R$**: Radix step (default is 8 bits).
Since $K$ and $R$ are often constants for standard 64-bit integers, the algorithm performs with **near-linear time complexity**.

### Space Complexity: $O(N + 2^R)$
- **$O(N)$**: Required for temporary bucket storage during distribution.
- **$O(2^R)$**: Memory for the bucket pointers (256 pointers for an 8-bit radix).

---

## 🚀 Features

- **Bit-length grouping** — Groups numbers by their bit length for better cache locality
- **Configurable radix** — Adjustable `radix_bits` parameter to balance time and memory
- **Handles signed integers** — Correctly sorts positive, negative, and zero values
- **Stable sort** — Preserves relative order of equal elements
- **No dependencies** — Pure standard library implementation

## 📊 Performance

Benchmark results on random integers (Python 3.14, radix_bits=8):

| Array Size | RageSort (ms) | QuickSort (ms) |
| :--- | :---: | :---: |
| 1,000 | 1.32 | 0.90 |
| 10,000 | 8.64 | 13.72 |
| 100,000 | 81.13 | 171.49 |
| 500,000 | 462.76 | 943.11 |

