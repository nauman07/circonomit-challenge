
# Task 2: Execution & Caching Strategy

## 🔍 Objective

To run simulations efficiently, you should: - Run calculated attributes in the right order - Avoid recalculating things that don't need to be recalculated - Support parallelism when you can.
---

##  Strategy

### 1. **Execution Layer**
All execution logic is handled in Python. In real systems, this could be moved to a microservice or database layer.

### 2. **Caching Intermediate Results**

#### Why Use Caching?

When running simulations:
- Many attributes are **reused** across scenarios.
- Re-evaluating the same calculations wastes time and resources.
- Caching improves performance and responsiveness.

#### What Kind of Caching?

- We use an **in-memory dictionary** as the cache.
- It stores results of previously evaluated attributes (keyed by full attribute name).
- If a dependency hasn't changed, the value can be reused.

#### Scaling the Cache
As system complexity grows:
- Replace in-memory cache with distributed caching layers (e.g., Redis, Memcached)
- Add cache invalidation rules when:
  - Inputs are updated
  - Dependencies are changed
- Consider versioning of simulations to trace changes without recomputing everything.


### 3. **Topological Sort**
#### Why Topological Sort?
- A DAG (Directed Acyclic Graph) represents dependencies between calculated attributes.
- To ensure correctness, calculations must be evaluated in order:
  - Inputs first
  - Calculated attributes next
  - Downstream values last
#### Runtime Complexity
- The algorithm we use is Kahn’s Topological Sort.
- Time Complexity:
  O(V + E)
  where:
  - V = number of attributes (nodes)
  - E = number of dependencies (edges)

#### Scaling with DAG
When scaling to thousands of attributes:
- Topological sort still runs in linear time with respect to size of model
- Store DAG in a graph database or structured index for faster lookups
- Parallelize non-dependent subgraphs for distributed computation

### 4. **Parallel Execution**
- Attributes that do not depend on each other can be computed in parallel.
- We use ThreadPoolExecutor to run independent nodes concurrently
- Future Improvement: Group and batch levels of DAG to:
  - Avoid thread starvation
  - Control concurrency better
- In big data contexts, use:
  - Apache Spark for DAG-based execution
  - Dask or Ray for Python-native task graphs

---

| Feature            | Why It Matters                                        |
| ------------------ | ----------------------------------------------------- |
| DAG + Topo Sort    | Prevents race conditions, ensures correct order       |
| Caching            | Saves compute time, avoids duplicate work             |
| Multithreading     | Speeds up simulation for large graphs                 |
| Scalable structure | Ready for transition to big-data, distributed compute |

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


