
# Task 2: Execution & Caching Strategy

## 🔍 Objective

Design an efficient approach to run simulations by:
- Executing calculated attributes in the right order
- Avoiding unnecessary recalculations
- Supporting parallelism where possible

---

## 🧠 Strategy

### 1. **Execution Layer**
All execution logic is handled in Python. In real systems, this could be moved to a microservice or database layer.

### 2. **Caching Intermediate Results**
- Cache attribute values after computation.
- Use a simple in-memory cache (dictionary) during evaluation.
- Only recompute if dependencies have changed.

### 3. **Topological Sort**
- We use a directed acyclic graph (DAG) to determine the execution order.
- Each node is a calculated attribute.
- Dependencies form directed edges.

### 4. **Parallel Execution**
- Attributes that do not depend on each other can be computed in parallel.
- We use Python’s `concurrent.futures.ThreadPoolExecutor` to parallelize groups of independent nodes.

---

## 🗂️ Project Structure

```
Task2_ExecutionCaching/
├── main.py         # Entry point: builds model, evaluates with caching
├── model.py        # Basic model for attributes/blocks
├── executor.py     # DAG traversal + execution with parallelism and cache
├── scenarios.py    # Sample override scenarios
└── explaination.md # Layman explanation of strategy
```

---

## 🚀 How to Run

```bash
python main.py
```

The simulation applies a scenario, executes attributes in topological order, and caches results.

---

## ✅ Features

- DAG-based dependency tracking
- Automatic execution order
- In-memory caching
- Support for multithreaded parallelism
