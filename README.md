# Caching Benchmark Algorithms

Python scripts comparing cached and uncached approaches to two classic problems: range-sum queries on an array and Fibonacci number computation.

## Contents

### `task1.py` — LRU-Cached Range Sum Queries

Generates a random array and a mix of random `Range` (sum query) and `Update` (point update) operations, then measures and compares the total execution time with and without an `lru_cache`-based cache for range-sum results.

### `task2.py` — Fibonacci: LRU Cache vs. Splay Tree

Implements a splay tree data structure from scratch and uses it to memoize Fibonacci results, comparing its performance against `functools.lru_cache` for several values of `n`. Results are printed as a table and plotted with `matplotlib`.

## Stack

- Python 3
- `matplotlib`
- `tabulate`

## Usage

```bash
pip install matplotlib tabulate
python task1.py
python task2.py
```
