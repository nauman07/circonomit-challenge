
class Attribute:
    def __init__(self, name, attr_type, value=None, formula=None, dependencies=None):
        self.name = name
        self.type = attr_type  # 'input' or 'calculated'
        self.value = value
        self.formula = formula
        self.dependencies = dependencies or []

class Block:
    def __init__(self, name):
        self.name = name
        self.attributes = {}

    def add_attribute(self, attr):
        self.attributes[attr.name] = attr

def load_blocks_from_scenario(scenario):
    # Create blocks
    energy = Block("Energy")
    costs = Block("Costs")

    # Define input attributes
    energy.add_attribute(Attribute("energy_price_per_kwh", "input", 0.20))
    energy.add_attribute(Attribute("kwh_used", "input", 1000))
    costs.add_attribute(Attribute("material_cost", "input", 500))

    # Define calculated attributes
    energy.add_attribute(Attribute(
        "energy_cost", "calculated", formula="energy_price_per_kwh * kwh_used",
        dependencies=["energy_price_per_kwh", "kwh_used"]
    ))

    costs.add_attribute(Attribute(
        "total_cost", "calculated", formula="material_cost + energy_cost",
        dependencies=["material_cost", "energy_cost"]
    ))

    # Apply scenario overrides
    all_blocks = {"Energy": energy, "Costs": costs}
    for attr_path, value in scenario["overrides"].items():
        block_name, attr_name = attr_path.split(".")
        all_blocks[block_name].attributes[attr_name].value = value

    return all_blocks
