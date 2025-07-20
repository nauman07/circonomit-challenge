class Attribute:
    def __init__(self, name, attr_type, formula=None, dependencies=None, value=None):
        self.name = name
        self.type = attr_type  # 'input' or 'calculated'
        self.formula = formula  # string representing calculation
        self.dependencies = dependencies or []  # list of attribute names
        self.value = value

    def __repr__(self):
        return f"<Attribute: {self.name} = {self.value}>"

class Block:
    def __init__(self, name):
        self.name = name
        self.attributes = {}

    def add_attribute(self, attr: Attribute):
        self.attributes[attr.name] = attr

    def __repr__(self):
        return f"<Block: {self.name} with {len(self.attributes)} attributes>"

def load_model():
    """Builds and returns a dictionary of blocks with attributes."""
    # Create blocks
    energy = Block("Energy")
    costs = Block("Costs")

    # Add attributes to Energy block
    energy.add_attribute(Attribute("energy_price_per_kwh", "input", value=0.18))
    energy.add_attribute(Attribute("kwh_used", "input", value=1000))
    energy.add_attribute(Attribute("energy_cost", "calculated",
                                   formula="energy_price_per_kwh * kwh_used",
                                   dependencies=["energy_price_per_kwh", "kwh_used"]))

    # Add attributes to Costs block
    costs.add_attribute(Attribute("material_cost", "input", value=500))
    costs.add_attribute(Attribute("total_cost", "calculated",
                                  formula="material_cost + energy_cost",
                                  dependencies=["material_cost", "energy_cost"]))

    return {
        "Energy": energy,
        "Costs": costs
    }

def apply_scenario(blocks, scenario):
    """Override input values in the model with those from the scenario."""
    for attr_path, new_value in scenario["overrides"].items():
        block_name, attr_name = attr_path.split(".")
        if block_name in blocks and attr_name in blocks[block_name].attributes:
            attr = blocks[block_name].attributes[attr_name]
            if attr.type == "input":
                attr.value = new_value
