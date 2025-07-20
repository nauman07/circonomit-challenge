from model import load_model, apply_scenario
from engine import SimulationEngine
from scenarios import SCENARIO_HIGH_ENERGY

def main():
    # Load base model with blocks and attributes
    blocks = load_model()

    # Apply scenario overrides
    scenario_name = "High Energy Price"
    print(f"Running simulation for scenario: {scenario_name}")
    apply_scenario(blocks, SCENARIO_HIGH_ENERGY)

    # Initialize simulation engine
    engine = SimulationEngine(blocks)

    # Run simulation
    results = engine.run_simulation()

    # Display final results
    print("\n--- Simulation Results ---")
    for block_name, block in results.items():
        print(f"\n[{block_name}]")
        for attr_name, attr in block.attributes.items():
            print(f"{attr_name}: {attr.value}")

if __name__ == "__main__":
    main()
