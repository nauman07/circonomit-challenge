
# Task 4: Product Thinking & Usability

## 🧠 Objective

Design an intuitive interface that enables **non-technical users** to:
- Set up models (Blocks, Attributes)
- Override input values (run Scenarios)
- Visualize calculation results and dependencies
- Compare outcomes and perform sensitivity analysis
- Understand system-wide impact of changes

---

## 🧩 Key Design Goals

1. **Clarity**
   - Minimize cognitive load with visual simplification
   - Replace jargon with guided descriptions and icons

2. **Guided Workflow**
   - Step-based flow for:
     1. Model Setup
     2. Scenario Definition
     3. Simulation Execution
     4. Result & Sensitivity Exploration

3. **Output Comparison**
   - Multi-scenario or multi-input comparisons
   - KPI-focused result panels with filtering options

4. **Sensitivity Analysis**
   - Vary one or more inputs across a range
   - Plot changes in outputs dynamically (e.g., line charts)

5. **Feedback Transparency**
   - Show cascading impacts and intermediate values
   - Trace output back to source with “Why did this change?” paths

6. **Explainability**
   - Hoverable tooltips for formulas, source values
   - Click-through to backtrack calculation logic

---

## Suggested Views (UI Components)

### 1. Model Builder
- Drag & drop blocks and attributes
- Add formulas with validation
- Real-time dependency map with cycle detection

### 2. Scenario Lab
- Clean form view to input override values
- Inline documentation/tooltips
- Ability to save/load scenarios
- Option to “compare with base” toggle

### 3. Simulation Dashboard
- Panel of calculated outputs
- Calculation trace for each output
- Toggle to include/exclude intermediate results

### 4. Sensitivity Analyzer
- Form to select:
  - Input variable (range of values)
  - Output KPIs to track
- Generate line chart showing how each output changes
- Multi-line comparison view

### 5. Output Filters & Comparison
- Allow user to select which metrics to display
- Group outputs by block or theme
- Highlight differences from baseline visually

---

## Bonus Task: Dependency DAG Visualization

- Directed graph view (DAG):
  - Nodes: Attributes
    - Blue = Input
    - Green = Calculated
  - Edges: Dependencies
- Hover: show value + formula
- Click: trace full upstream path

---

