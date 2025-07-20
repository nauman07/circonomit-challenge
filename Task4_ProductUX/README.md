
# Task 4: Product Thinking & Usability

## 🧠 Objective

Design an intuitive interface that enables **non-technical users** to:
- Set up models (Blocks, Attributes)
- Override input values (run Scenarios)
- Visualize calculation results and dependencies
- Understand system-wide impact of changes

---

## 🧩 Key Design Goals

1. **Clarity**
   - Avoid jargon, use visual cues
   - Display only relevant data per action

2. **Guided Workflow**
   - Wizard-style steps for:
     1. Model Setup
     2. Scenario Override
     3. Run Simulation
     4. Explore Results

3. **Feedback Transparency**
   - Visualize:
     - Dependencies (DAG)
     - Cascading changes
     - Bottlenecks or loops

4. **Explainability**
   - Enable "why did this change?" exploration
   - Allow users to trace outputs back to inputs

---

## Suggested Views

### 1. Model Editor
- Drag & drop interface to define Blocks and Attributes
- Formula builder with autocomplete
- Real-time validation of dependencies

### 2. Scenario Playground
- Table or form to override input values
- “Play” button to simulate

### 3. Result Explorer
- Panel of KPIs with:
  - Raw values
  - Calculation trace
- Interactive dependency map

### 4. Sensitivity Analyzer
- Sliders for input attributes
- Output charts are updating in real-time
- Tornado chart for impact comparison

---

## 🧭 Bonus Task: Visualizing Dependencies

We suggest using:
- **Network graph** (DAG) to show inputs → outputs
- Color-coded nodes:
  - Blue = Input
  - Green = Calculated
- Hover/click to see formulas and data lineage

---
