# 🧠 Explanation: How the Simulation Program Works

This simulation system is built to help businesses test different decisions and see how things might change when some inputs are modified. Think of it like a smart calculator that can connect different pieces of information and figure out how one change (like energy cost) affects the total cost of production.

---

## 🧱 What is the System Made Of?

### 1. Blocks and Attributes
- A **Block** is a group of related values (like `Energy` or `Costs`).
- An **Attribute** is a specific value inside that group (e.g., `energy price per kWh` or `total cost`).

Attributes can be:
- **Inputs**: Numbers the user can change.
- **Calculated**: Numbers that are calculated based on other values.

---

## 🧪 What Does It Do?

Let’s say we want to know how a rise in energy price affects the total production cost. Instead of doing the math by hand every time, this system:
1. Builds a network of all values and how they depend on each other.
2. Lets you override input values to test a different “scenario” (like high energy prices).
3. Recalculates all the connected values in the correct order.

---

## ⚙️ How It Works Internally

### Step 1: Load the Base Model
- We define two blocks: **Energy** and **Costs**.
- Some values are fixed inputs (like base energy price).
- Others are calculated using formulas (like `total_cost = material_cost + energy_cost`).

### Step 2: Apply a Scenario
- A “scenario” is just a change to some of the input values.
- For example: “What if energy price goes up?”

### Step 3: Figure Out the Right Order
- Some values depend on others.
- The system figures out which values to calculate first by looking at the dependencies.

### Step 4: Run the Simulation
- All calculated values are updated based on your new inputs.
- Final results are printed so you can compare and analyze.

---

## 📈 What Problem Does This Solve?

Imagine you're a decision-maker in a company and you want to answer:
> “What happens to our costs if energy prices go up next month?”

This tool gives you that answer instantly—and lets you try out as many scenarios as you want.

It saves time, avoids manual errors, and makes complex decisions easier to understand.

---

## 🧰 Files Explained

| File             | Purpose                                               |
|------------------|--------------------------------------------------------|
| `main.py`        | Runs the simulation and prints results                |
| `model.py`       | Defines the data structure (blocks and attributes)    |
| `engine.py`      | Calculates the right order and performs the math      |
| `scenarios.py`   | Contains input changes for test cases                 |

---

## ✅ Summary

This program lets you model real-world business logic in a flexible and reusable way. Whether you're simulating costs, energy usage, or supply chain decisions—this tool can help you explore “what if?” scenarios easily.
