
# 🧠 ASCII Flowchart: End-to-End System Data Flow

```
[User Input]
     |
     v
[NLP Parser (Task 3)]
     |
     v
[Structured Model (Blocks + Attributes)]
     |                          |
     |                          v
     |               [Scenario Overrides (Task 1)]
     |                          |
     |                          v
     +------------------>[Calculation Engine (Task 2)]
                                |
                                v
                    [Execution DAG & Caching]
                                |
                                v
                       [Simulation Results]
                                |
                                v
                   [Visualization Layer (Task 4)]
```

---

## 💡 Summary
This flow represents how Circonomit’s simulation engine processes a business problem from start to finish:

- **Natural Language Input** is parsed into structured blocks & attributes.
- **Overrides** allow what-if scenario modeling.
- **The Engine** computes values with dependency management and caching.
- **Visualization** helps decision-makers interpret the results.

Each step corresponds to a dedicated module and task in your challenge.
