
from parser_utils import extract_attributes_and_formulas

def extract_model_structure(text):
    blocks = set()
    attributes = []

    extracted = extract_attributes_and_formulas(text)

    for item in extracted:
        attr_name = item['name']
        attr_type = item['type']
        formula = item.get('formula')

        # Infer block by name prefix (simplified logic)
        if "energy" in attr_name:
            blocks.add("Energy")
        elif "material" in attr_name or "total" in attr_name:
            blocks.add("Costs")

        attr_entry = {
            "name": attr_name,
            "type": attr_type
        }
        if formula:
            attr_entry["formula"] = formula
        attributes.append(attr_entry)

    return {
        "blocks": list(blocks),
        "attributes": attributes
    }
