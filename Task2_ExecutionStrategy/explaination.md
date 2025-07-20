
# 🧠 Explanation: Execution & Caching Strategy

## 🧩 What Problem Are We Solving?

If STK wants to test a business choice, like "What happens if energy prices go up?" With this change, our system can figure out new results, such as total costs. But some of these numbers depend on others, so we need to figure them out in the right order and quickly.

---

## ⚙️ How Does It Work?

### Step 1: Understand Dependencies
Some values depend on others. For example:
- `energy_cost = energy_price_per_kwh * kwh_used`
- `total_cost = material_cost + energy_cost`

We must first compute `energy_cost` before we can calculate `total_cost`.

We build a graph that shows what depends on what.

---

### Step 2: Sort Them in the Right Order
We use a method called **topological sort** to decide the correct order:
- First: calculate things that don’t depend on anything (inputs)
- Then, one by one, calculate the values that depend on those

---

### Step 3: Cache What You Already Know
To avoid repeating calculations:
- We store each computed value in a cache memory
- If the same value is needed again, we just read it from the cache

---

### Step 4: Speed Up with Parallel Computing
- If some values don’t depend on each other, we compute them **in parallel**
- This makes the simulation faster, especially when dealing with big models

---

## 🧰 What’s Inside the Code?

| File            | What It Does |
|------------------|--------------|
| `main.py`        | Runs the scenario and prints results |
| `model.py`       | Defines blocks and attributes (inputs/calculations) |
| `executor.py`    | Manages dependency graph, caching, and order of execution |
| `scenarios.py`   | Holds test scenarios with overridden inputs |

---

## ✅ Why It Matters

This strategy lets businesses:
- Make complex simulations faster
- Avoid recalculating the same thing twice
- Easily explore “what if?” scenarios
- Understand how one change flows through the system

This system is like a smart calculator that:
- Knows the order of operations
- Remembers past answers
- Works faster by multitasking

