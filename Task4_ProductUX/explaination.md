
# 🧠 Explanation: Product Thinking & Usability

## What Are We Building?

We're building a **simulation platform** for non-technical users.  
Think of it like Excel — but smarter, visual, and way easier to use.

Users want to:
- Enter or override data (like energy prices or labor hours)
- Get insights and totals (like total cost)
- Understand why things changed
- See how changes affect other areas

---

## Our Design Philosophy

### 1. Keep It Simple
- Speak the user’s language — not technical formulas.
- Use tooltips and guided flows to onboard new users.

### 2. Guide the User
- Design step-by-step flows:
  1. Create Model (blocks & attributes)
  2. Override values for different scenarios
  3. Run simulations
  4. Explore the results visually

### 3. Visual Thinking
- Show graphs, charts, and flows instead of tables
- Color-coded nodes for different attribute types
- Sliders for tweaking input values and instantly seeing effects

---

## Example Use Case

💬 Business user says:
> “I want to test what happens if electricity gets more expensive.”

🛠 They open the **Scenario Playground**, change `energy_price_per_kwh`, and click **Simulate**.

🎯 They go to **Result Explorer**, where:
- Total cost updates
- They see a tree that explains:
  - energy_price_per_kwh → energy_cost → total_cost

---

## Bonus: Visualizing Dependencies

We show a **graph** with arrows:
- Inputs in blue
- Calculated values in green
- Arrows show how each value flows into the next

Hovering shows:
- Description
- Current value
- Formula used

---

## Why This Matters

This helps users:
- Trust the model
- Understand results
- Ask better questions
- Make smarter decisions

No code. No SQL. No confusion. Just insights.

