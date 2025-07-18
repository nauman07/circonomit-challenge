# Task 1: Extend the Data Model for Simulations

## 🧩 Problem Overview
The existing model contains:
- **Blocks**: Containers that group related attributes (e.g., `Energy`, `Production`, `Costs`)
- **Attributes**: Elements within a block. Can be either:
  - **Input attributes**: Set directly by the user or data feed
  - **Calculated attributes**: Derived from other attributes via a formula

We are to extend this model to support:
- Simulation scenarios with input overrides
- Tracking of overrides
- Dependency handling (including avoidance of cycles and managing feedback loops)

---

## ✅ Proposed Data Model Extension

### 🔷 New Components

#### 1. `Scenario`
Represents a simulation context. Contains a mapping of attribute overrides.
```json
{
  "scenario_id": "S1",
  "name": "High Energy Price",
  "overrides": {
    "Energy.energy_price_per_kwh": 0.22,
    "Production.shift_hours": 20
  }
}
```

#### 2. `Attribute`
Each attribute is extended with metadata:
- `type`: input | calculated
- `formula`: (if calculated)
- `dependencies`: list of other attributes it depends on
- `value`: default/base value

```json
{
  "block": "Costs",
  "name": "total_cost",
  "type": "calculated",
  "formula": "material_cost + energy_cost",
  "dependencies": ["Costs.material_cost", "Energy.energy_cost"],
  "value": null
}
```

#### 3. `CalculationGraph`
A directed acyclic graph (DAG) constructed at runtime to:
- Determine execution order of attributes
- Detect cycles and feedback loops

---

## ⚙️ Simulation Logic
1. **Load base model** (blocks + attributes)
2. **Apply scenario overrides** to input attributes
3. **Construct dependency graph** from calculated attributes
4. **Topological sort** to determine safe execution order
5. **Evaluate formulas**, caching intermediate results

---

## 🔁 Feedback Loops & Cyclic Dependencies
To handle feedback loops:
- Mark nodes as `iterative`
- Define convergence criteria (e.g., value change < ε)
- Use fixed-point iteration:
  - Run dependent calculations multiple times until convergence

Preventing cycles:
- Use DAG validation
- Raise exception if hard cyclic dependency is detected without convergence logic

---

## 🗂️ Storage of Overrides
- Store scenario objects as JSON files or in a NoSQL store
- Keep history of overrides and simulation runs for traceability
- Include metadata: timestamp, user, scenario notes

---

## 📦 Example JSON Snippets
**Base Attribute (input):**
```json
{
  "block": "Energy",
  "name": "energy_price_per_kwh",
  "type": "input",
  "value": 0.18
}
```

**Base Attribute (calculated):**
```json
{
  "block": "Energy",
  "name": "energy_cost",
  "type": "calculated",
  "formula": "energy_price_per_kwh * kwh_used",
  "dependencies": ["Energy.energy_price_per_kwh", "Energy.kwh_used"]
}
```

**Scenario:**
```json
{
  "scenario_id": "S2",
  "name": "CO2 Regulation Increase",
  "overrides": {
    "CO2.carbon_cost_per_unit": 50
  }
}
```

---

## 🧠 Summary
This model extension enables:
- Dynamic simulation scenarios
- Clear override management
- Deterministic evaluation via DAG
- Handling of feedback loops
- Scenario traceability and reproducibility
