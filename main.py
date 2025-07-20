
from model import load_blocks_from_scenario
from scenarios import SCENARIO_HIGH_ENERGY
from executor import SimulationExecutor

def print_results(blocks):
    print("\nFinal Computed Values:")
    for block in blocks.values():
        print(f"\nBlock: {block.name}")
        for attr in block.attributes.values():
            print(f"  {attr.name}: {attr.value}")

if __name__ == "__main__":
    # Load base model and apply scenario
    blocks = load_blocks_from_scenario(SCENARIO_HIGH_ENERGY)

    # Execute simulation with caching and parallel support
    engine = SimulationExecutor(blocks)
    engine.run_simulation()

    # Print results
    print_results(blocks)
