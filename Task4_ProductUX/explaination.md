# 🧠 Explanation: Product Thinking & Usability

## What Are We Building?

We're building a **simulation platform** tailored for **non-technical decision-makers** to:
- Define how business variables interact (e.g., energy cost depends on usage and price)
- Override input values in real-world scenarios
- Visualize impacts, trace logic, and test hypotheses
- Compare different “what-if” simulations intuitively

---

## Our Design Philosophy

### 1. Speak Their Language
- Avoid math or code in the UI
- Show “energy price × consumption = energy cost” — not raw formulas
- Use tooltips, examples, and glossary help

### 2. Guide the Journey
A wizard-style UI walks users through:
1. **Model Setup** — define blocks, inputs, and calculations
2. **Scenario Creation** — override variables (e.g., prices, hours)
3. **Simulation Run** — execute the model and get values
4. **Result Analysis** — view metrics and trace logic

Each step builds on the last to promote understanding.

### 3. Visual First
- Replace data tables with:
  - Live charts
  - Dependency graphs
  - KPI cards
- Interactive flows show how variables affect outcomes
- Filters let users focus only on outputs that matter to them

---

## Example Use Case

💬 Business user says:  
> “I want to test how rising electricity costs affect our production spend.”

They:
1. Open the **Scenario Lab** and change `energy_price_per_kwh`
2. Hit **Simulate**
3. Navigate to **Result Explorer** and see:

- `energy_cost` and `total_cost` updated
- A **trace graph** shows:  
  `energy_price_per_kwh → energy_cost → total_cost`

4. They use the **Sensitivity Analyzer** to run the simulation over a range (e.g., 0.15–0.30 €/kWh), and view results as a **line chart**.

---

## Bonus: Dependency Graphs & Smart Filtering

We visualize the attribute flow as a DAG:
- **Blue** = Inputs  
- **Green** = Calculated values  
- **Edges** = Calculation dependencies

Features:
- Hover: See name, value, and logic
- Filters: Let users pick which KPIs they want to focus on
- Toggles: Highlight paths that changed from base to scenario

---

## Why It Works

✅ For the user:
- It’s simple: no code, no formulas to memorize  
- It’s fast: tweak → simulate → see effect  
- It’s transparent: users know why a number changed  
- It’s explainable: users can confidently present results to stakeholders

---

🎯 Final Thought:
We’re not just building software.  
We’re building a **thinking tool** — to help people make better business decisions through clarity, curiosity, and computation.

