# Define a sample simulation scenario for overriding input values
SCENARIO_HIGH_ENERGY = {
    "scenario_id": "S1",
    "name": "High Energy Price",
    "overrides": {
        "Energy.energy_price_per_kwh": 0.25,
        "Energy.kwh_used": 1200,
        "Costs.material_cost": 600
    }
}

# You can add more scenarios if needed
SCENARIO_BASELINE = {
    "scenario_id": "S0",
    "name": "Baseline",
    "overrides": {}
}
