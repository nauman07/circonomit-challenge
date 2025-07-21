
# 🧪 Demo Script: Product Flow

👤 Meet Nauman — a supply chain analyst at a mid-sized manufacturer.

---

### Step 1: Create Model
Nauman opens the “Model Builder” and defines a few blocks:
- Block: Energy
  - Input: energy_price_per_kwh
  - Input: kwh_used
  - Calculated: energy_cost = energy_price_per_kwh * kwh_used
- Block: Costs
  - Input: material_cost
  - Calculated: total_cost = energy_cost + material_cost

---

### Step 2: Setup Scenario
Nauman opens the “Scenario Playground”:
- He sets `energy_price_per_kwh = 0.22` and `kwh_used = 1200`
- He clicks “Run Simulation”

---

### Step 3: View Results
Nauman sees:
- `energy_cost = 264.0`
- `total_cost = 864.0`

---

### Step 4: Explore Impacts
- He opens the DAG: sees that total_cost depends on energy_cost + material_cost
- He adjusts `kwh_used` with a slider and watches the results update live

---

### Step 5: Export
- Nauman downloads the result report and shares it with the CFO, Mr Thomas.
