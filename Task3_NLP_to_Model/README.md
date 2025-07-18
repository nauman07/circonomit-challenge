# Task 3: Natural Language to Model

## 🎯 Objective
Design an approach to convert human language (text, chat, or spoken input) into a structured data model composed of:
- **Blocks**
- **Attributes** (input or calculated)
- **Relationships** (formulas, dependencies)

---

## 🧠 Key Challenges
- Identify relevant business terms and concepts
- Disambiguate vague statements
- Map language constructs to formal structures (variables, logic)

---

## 🧱 Proposed Pipeline Architecture

### Step 1: **Preprocessing**
- Clean text (remove noise, normalize units)
- Segment into meaningful instructions/statements

### Step 2: **Entity Extraction**
Use Named Entity Recognition (NER) or LLM prompt-based techniques to extract:
- Domain-specific terms (e.g., `energy price`, `shift hours`)
- Logical structures (e.g., “if... then...”, “depends on”, “is calculated as”)
- Units, thresholds, conditions

### Step 3: **Classification & Typing**
- Classify extracted terms as:
  - **Block** (group/category)
  - **Attribute** (within block)
  - **Relationship** (formula or dependency)
- Determine type: `input` or `calculated`

### Step 4: **Mapping to Model Format**
Generate formal structures:
```json
{
  "block": "Energy",
  "attribute": "energy_cost",
  "type": "calculated",
  "formula": "price_per_kwh * usage_kwh",
  "dependencies": ["price_per_kwh", "usage_kwh"]
}
```

---

## 💬 Example Input
> "If the energy price per kWh increases above 0.25, the production should switch to night shift."

### Result:
- Block: `Energy`, Attribute: `price_per_kwh`, Type: `input`
- Block: `Production`, Attribute: `shift_schedule`, Type: `calculated`
- Rule: `IF Energy.price_per_kwh > 0.25 THEN Production.shift_schedule = 'night'`

---

## 🔧 Tools and Techniques
| Task | Tool |
|------|------|
| NLP Base | spaCy / HuggingFace Transformers |
| LLM Reasoning | OpenAI / Claude / Mistral API |
| Mapping Rules | Custom prompt-based templates or rules engine |
| Integration | Convert output into JSON schema for simulation engine |

---

## 🔄 Feedback Loop
1. Extract candidate structures
2. Let user confirm or correct mappings (semi-automated)
3. System learns over time (fine-tune prompts or improve rule coverage)

---

## ✅ Summary
This pipeline allows:
- Extracting structured models from messy natural input
- Connecting knowledge sources (docs, chat) to technical systems
- Supporting non-technical users in creating simulation-ready models
