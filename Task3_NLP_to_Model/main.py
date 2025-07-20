
from nlp_engine import extract_model_structure

if __name__ == "__main__":
    # Example natural language input
    input_text = """
    The energy cost is calculated by multiplying the price per kWh and the number of kilowatt-hours used.
    Total cost is the sum of material cost and energy cost.
    """

    print("Input Text:")
    print(input_text)

    print("\nExtracted Model Structure:")
    structure = extract_model_structure(input_text)
    for attr in structure["attributes"]:
        print(f" - {attr['name']} ({attr['type']})", end="")
        if "formula" in attr:
            print(f": {attr['formula']}")
        else:
            print()
