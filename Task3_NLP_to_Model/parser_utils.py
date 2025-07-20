
import re

def extract_attributes_and_formulas(text):
    attributes = []

    # Example pattern matching to simulate NLP
    if "energy cost" in text.lower():
        attributes.append({
            "name": "energy_price_per_kwh",
            "type": "input"
        })
        attributes.append({
            "name": "kwh_used",
            "type": "input"
        })
        attributes.append({
            "name": "energy_cost",
            "type": "calculated",
            "formula": "energy_price_per_kwh * kwh_used"
        })

    if "total cost" in text.lower():
        attributes.append({
            "name": "material_cost",
            "type": "input"
        })
        attributes.append({
            "name": "total_cost",
            "type": "calculated",
            "formula": "material_cost + energy_cost"
        })

    return attributes
