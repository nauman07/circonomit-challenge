# 🧠 Explanation: How the Simulation Program Works

Companies can use this simulation system to try out different choices and see how things might change when they change some inputs. It's like a smart calculator that can link different pieces of information and figure out how one change, like the cost of energy, affects the total cost of making something.

---

## 🧱 What is the System Made Of?

### 1. Blocks and Attributes
- A **Block** is a group of related values like `Energy` or `Costs`.
- An **Attribute** is a specific value inside that group, e.g., `energy price per kWh` or `total cost`.

Attributes can be:
- **Inputs**: Numbers the user can change.
- **Calculated**: Numbers that are calculated based on other values.

---

## 🧪 What Does It Do?

Suppose we are interested in the impact of rising energy prices on the overall cost of production. Rather than calculating the numbers by hand each time, this system:
1. Creates an interconnected network of all values and their interdependencies.
2. If you want to test a different "case," such as high energy prices, you can modify the input values.
3. Correctly recalculates all of the linked values.

---

## ⚙️ How It Works Internally

### Step 1: Load the Base Model
- We define two blocks: **Energy** and **Costs**.
- Some values are fixed inputs, like the base energy price.
- Others are calculated using formulas such as `total_cost = material_cost + energy_cost`.

### Step 2: Apply a Scenario
- A “scenario” is just a change to some of the input values.
- For example: “What if energy price goes up?”

### Step 3: Figure Out the Right Order
- Some values depend on others.
- The system figures which values to calculate first by looking at the dependencies.

### Step 4: Run the Simulation
- All calculated values are updated based on your new inputs.
- Final results are printed so you can compare and analyze.

---

## 📈 What Problem Does This Solve?

Imagine a decision-maker at STK, and you want to answer:
> “What happens to our costs if energy prices go up next month?”

This tool gives you the answer right away and lets you try out as many situations as you want.

It saves time, keeps people from making mistakes by hand, and makes hard decisions easier to understand.

---

## 🧰 Files Explained

| File             | Purpose                                               |
|------------------|--------------------------------------------------------|
| `main.py`        | Runs the simulation and prints results                |
| `model.py`       | Defines the data structure blocks and attributes      |
| `engine.py`      | Calculates the right order and performs the math      |
| `scenarios.py`   | Contains input changes for test cases                 |

---

## ✅ Summary

This program lets STK model real-world business logic in a way that is flexible and can be used again and again. This tool makes it easy to look at "what if?" scenarios, whether you're simulating costs, energy use, or supply chain decisions.
