
# Task 3: From Natural Language to Model

## 🧠 Goal

Design a system that takes natural language input (e.g. documents, chat messages, etc.) and extracts structured knowledge that can be translated into simulation-ready models made of:
- Blocks
- Attributes (input / calculated)
- Relationships (dependencies)

---

## 🛠️ Strategy Overview

1. **Text Ingestion**
   - Input comes from chat, documents, or audio (transcribed).
   - Example: "The energy cost is calculated by multiplying the price per kWh and the total kWh used."

2. **NLP Processing**
   - Sentence parsing: extract nouns and verbs.
   - Named Entity Recognition: identify potential variables and units.
   - Dependency analysis: find relationships (formulas and calculation flows).

3. **Knowledge Extraction**
   - Extract attributes and classify them:
     - Inputs: direct user-provided numbers
     - Calculated: inferred from verbs (e.g. multiply, add, subtract)
   - Extract formulas and dependencies.

4. **Mapping to Model**
   - Attributes are added into appropriate Blocks.
   - Dependencies form edges in the calculation graph.
   - Output can be JSON or Python structure.

---

## 📦 Folder Structure

```
Task3_NLPtoModel/
├── main.py           # Demo entry: simulate extraction from text
├── nlp_engine.py     # Extracts attributes, formulas, and structure from text
├── parser_utils.py   # Helper functions for tokenizing, NER, pattern matching
├── sample_input.txt  # Example sentence/document input
├── explaination.md   # Layman's explanation of this approach
└── README.md         # This documentation
```

---

## 🔍 Sample Input

```
"The energy cost is calculated by multiplying the price per kWh and the number of kilowatt-hours used. Total cost is the sum of material cost and energy cost."
```

## 🧾 Sample Output

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

## 🚀 Next Steps

- Add `main.py` to run a demo extraction
- Build minimal NLP parser for structured model creation
