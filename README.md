# Circonomit Hiring Challenge Repository

My answers to the Circonomit hiring challenge are in this repository. The goal of the challenge is to create a modular simulation framework based on Circonomit's mission, which is to help businesses think about decisions in terms of more than just financial outcomes, such as systemic dependencies, constraints, and second-order effects.

There are four tasks and one bonus question in the challenge. There is a folder for each task, and each folder has a README.md file that explains how to do the task.

---

## Repository Structure

```
circonomit-challenge/
│
├── Task1_ExtendDataModel/
│   └── README.md        # Data model extension for scenario based simulation
│
├── Task2_ExecutionStrategy/
│   └── README.md        # Strategy for computation orchestration, caching, parallelism
│
├── Task3_NLP_to_Model/
│   └── README.md        # Translating natural language into structured models
│
├── Task4_ProductUX/
│   └── README.md        # Product thinking and user interface design
│
└── Flow.png             # Flow Diagram of how the solution is working from input to output.
│
└── README.md            # Main documentation
│
└── system_data_flow.md  # Flow of how the solution is working from input to output.
```

---

## Understanding STK's Modeling Approach

STK's system can be understood as a two-layered decision infrastructure:

### 1. **Computation Layer**
- Responsible for evaluating the numerical and logical dependencies between variables.
- Attributes can be **inputs** or **calculated**.
- Calculated attributes can depend on other attributes, forming **directed acyclic graphs (DAGs)** or sometimes feedback loops.
- The system must support **overrides** for scenario modeling.

### 2. **Knowledge Layer**
- Encodes domain knowledge using natural language, external documentation, or user dialogue.
- Helps transform abstract, human concepts ("if energy cost rises, switch production mode") into formal models.
- Relies on **language models, NLP tools**, and **semantic mapping**.

### Core Building Blocks
- **Blocks** = Groups of related attributes (e.g., `EnergyModule`, `CostBlock`, `SupplyChain`)
- **Attributes** = Variables within blocks. They may be user inputs or derived through formulas.
- **Scenarios** = Sets of overrides for a given simulation context.
- **Simulation Engine** = Calculates the network of dependencies based on inputs and overrides.

---

## How to Navigate the Repo
- Each task folder includes a detailed explanation (`README.md`) and supporting files (e.g., diagrams, pseudo-code, or scripts).
- You can explore tasks independently, but they are logically connected:
  - Task 1 provides the modeling foundation
  - Task 2 defines the execution strategy
  - Task 3 explores the NLP interface to feed into Task 1
  - Task 4 focuses on making the system usable by business users

---
