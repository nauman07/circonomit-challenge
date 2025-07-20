
# 🧠 Explanation: Natural Language to Simulation Model

## What Are We Trying to Do?

Business users think in sentences — not code.

For example:
> "The energy cost is calculated by multiplying price per kWh and the energy consumed."

We want to turn this human language into a structured format that a simulation engine can use.

---

## How Does It Work?

### 1. Input
We accept simple English sentences from documents or conversations.

Example:
```
The energy cost is calculated by multiplying the price per kWh and the number of kilowatt-hours used.
Total cost is the sum of material cost and energy cost.
```

---

### 2. Parse the Text
Using rule-based patterns, we:
- Extract key nouns as **attributes**
- Classify them as either:
  - **Inputs** (given by user or sensor)
  - **Calculated** (derived using a formula)
- Identify **formulas** and **dependencies**

---

### 3. Output the Model
We turn the extracted data into structured blocks and attributes.

Example Output:
```json
{
  "blocks": ["Energy", "Costs"],
  "attributes": [
    {"name": "energy_price_per_kwh", "type": "input"},
    {"name": "kwh_used", "type": "input"},
    {"name": "energy_cost", "type": "calculated", "formula": "energy_price_per_kwh * kwh_used"},
    {"name": "material_cost", "type": "input"},
    {"name": "total_cost", "type": "calculated", "formula": "material_cost + energy_cost"}
  ]
}
```

---

## Why It’s Powerful

With this translation layer:
- Users don’t need to code models manually
- Domain experts can describe processes in English
- Our engine turns that into structured logic automatically

This bridges the gap between business logic and technical modeling.

