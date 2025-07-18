# Task 4: Product Thinking & Usability (with Bonus: Visualizations)

## 🧭 Objective
Design an intuitive interface that allows non-technical users to:
- Define models (Blocks and Attributes)
- Create and run simulation scenarios
- Understand results and underlying dependencies
- Visualize feedback loops and sensitivity of outcomes

---

## 🧩 User Persona
- Role: Controller, CFO, Business Planner
- Background: Not a programmer, familiar with Excel, dashboards, and decision models
- Goal: Understand trade-offs, simulate scenarios, and interpret results

---

## 🖼️ Interface Overview

### 1. **Model Builder Interface**
- Visual layout for Blocks (columns or cards)
- Drag-and-drop Attribute creation
- Attribute type toggle (input vs calculated)
- Inline formula builder with autocomplete (e.g., `= price_per_kwh * kwh_used`)
- Dependency highlights

### 2. **Scenario Manager**
- List of existing scenarios
- Clone & edit functionality
- Input override interface (side-by-side with base value)
- Tagging for scenario themes (e.g., "CO2 regulation", "energy shock")

### 3. **Simulation Execution Panel**
- Run button with real-time progress bar
- Summary of key metric changes
- Optional: toggle to enable iterative convergence handling (for feedback loops)

### 4. **Results Dashboard**
- Table view of final attribute values
- KPI tracker with deltas from base case
- Export to CSV/Excel or shareable report link

---

## 🌀 Bonus: Visualizations for Dependencies & Sensitivity

### A. **Dependency Graph Viewer**
- Nodes = Attributes
- Edges = Dependencies
- Use D3.js or similar for interactive display
- Click on a node shows:
  - Formula
  - Inputs
  - Override status

### B. **Feedback Loop Highlighter**
- Cyclic edges in red
- Tooltip with convergence criteria & results (e.g., iterations, delta)

### C. **Sensitivity Explorer**
- Slider-based inputs with real-time output updates
- Tornado chart: shows most sensitive inputs for a selected KPI
- Heatmaps for 2D parameter sweeps

---

## 🛠️ UX Principles
- Progressive disclosure: show complexity only when needed
- Safe editing: changes are draft until saved
- Undo history for simulations
- Tooltips & example templates ("Start from energy model")
- AI assistant panel for suggestions (integrated with NLP from Task 3)

---

## ✅ Summary
This interface enables non-technical decision-makers to:
- Build meaningful models quickly
- Simulate and compare scenarios
- Visualize how everything connects
- Trust the output by understanding the logic behind it
