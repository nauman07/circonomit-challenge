# Task 2: Execution & Caching Strategy

## 🎯 Goal
Design an efficient and scalable computation layer for evaluating models defined as Blocks and Attributes. The system should:
- Execute calculations based on dependencies
- Cache intermediate results
- Enable parallelization where possible

---

## 🧱 Assumptions
- Each **calculated attribute** depends on zero or more other attributes
- Input values may be overridden by a **scenario**
- A **directed acyclic graph (DAG)** represents dependencies

---

## ⚙️ Computation Stack Design

### 📍 Where Should Computation Happen?
**Primary choice:** Application Layer (Python engine)

**Why?**
- Easier to manipulate DAGs, run custom logic, and perform iterative convergence
- Enables tight integration with both frontend (user inputs) and backend (data sources)

**Secondary options:**
- For large-scale workloads: offload to a distributed engine (e.g., Dask, Ray)
- For persisted results: store derived outputs in a database or cache (e.g., Redis, PostgreSQL)

---

## 🔄 Caching Strategy

### What to Cache?
- **Intermediate results** of calculated attributes
- Cache at **attribute level**, using a hash of:
  - Formula string
  - Input values (from scenario)

### How to Cache?
- In-memory cache (e.g., Python `functools.lru_cache`, or Redis for cross-session caching)
- Cache key = hash(attribute_id + formula + input values)
- Use `dirty flags` or dependency graph versioning to invalidate affected nodes only

---

## ⚡ Parallelization Strategy

### Execution Plan:
- Perform a **topological sort** of the DAG
- Identify **independent nodes** (same level in the DAG)
- Use a **task queue** (e.g., `concurrent.futures.ThreadPoolExecutor`) to evaluate independent attributes in parallel

### Example:
```
     A
    / \
   B   C
    \ /
     D
```
- A → level 0 (input)
- B, C → level 1 (can be computed in parallel)
- D → level 2 (depends on B, C)

---

## 🧪 Iterative Evaluation (Feedback Loops)
- Identify cycles in the DAG
- For any **iterative block**:
  - Run recalculations until **value change < ε** or max iterations reached
- Store convergence metadata per node (delta, iteration count)

---

## 🛠️ Tooling Suggestion
- Language: Python
- Graph lib: `networkx`
- Caching: `functools.lru_cache` (local), Redis (shared)
- Parallelism: `ThreadPoolExecutor`, `asyncio`, or Dask for scalability

---

## ✅ Summary
| Component | Strategy |
|----------|----------|
| Computation | Application layer (Python), with DAG execution |
| Caching | Attribute-level, hash-based cache keys |
| Parallelism | Topo-sorted layers → parallel execution of independent nodes |
| Feedback loops | Fixed-point iteration with convergence checks |

This strategy balances performance, transparency, and correctness. It scales well from single-scenario runs to large batch simulations.
