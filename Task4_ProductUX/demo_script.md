# 🧪 Demo Script: Product Flow

👤 Meet Nauman — a supply chain analyst at a mid-sized manufacturing firm using STK to understand cost drivers and improve decision-making.

---

### 🛠️ Step 1: Model Setup
Nauman opens the **Model Builder** and configures two functional blocks:

#### 🔹 Block: Energy
- `energy_price_per_kwh` → *Input*
- `kwh_used` → *Input*
- `energy_cost = energy_price_per_kwh * kwh_used` → *Calculated*

#### 🔹 Block: Costs
- `material_cost` → *Input*
- `total_cost = energy_cost + material_cost` → *Calculated*

The DAG viewer auto-updates to show relationships visually.

---

### 🧪 Step 2: Define Scenario
Nauman switches to the **Scenario Playground**:
- Enters `energy_price_per_kwh = 0.22`
- Enters `kwh_used = 1200`
- Enters `material_cost = 600`
- Clicks **“Run Simulation”**

---

### 📊 Step 3: Results Panel
The system computes:

| Attribute     | Value   |
|---------------|---------|
| energy_cost   | 264.0   |
| total_cost    | 864.0   |

Each metric includes a trace icon 🔍 to backtrack its inputs.

---

### 📈 Step 4: Sensitivity Analysis
In the **Sensitivity Analyzer**, Nauman selects:
- Input to vary: `energy_price_per_kwh` (0.15 to 0.30)
- Outputs to track: `total_cost`

He sees a live **line plot** showing how rising energy prices increase cost.
He toggles “Compare With Baseline” to see both scenarios side by side.

---

### 🧠 Step 5: Explain & Export
- Opens **DAG Viewer** to trace dependency paths
- Clicks **“Why did this change?”** under `total_cost` and reviews formula chain
- Downloads the results as PDF/CSV
- Shares insights with CFO, Mr. Thomas

