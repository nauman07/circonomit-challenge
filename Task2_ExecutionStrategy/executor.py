from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict, deque

class SimulationExecutor:
    def __init__(self, blocks):
        self.blocks = blocks
        self.cache = {}
        self.graph = defaultdict(list)
        self.in_degree = defaultdict(int)
        self.build_dependency_graph()

    def build_dependency_graph(self):
        for block in self.blocks.values():
            for attr in block.attributes.values():
                if attr.type == "calculated":
                    for dep in attr.dependencies:
                        self.graph[dep].append(f"{block.name}.{attr.name}")
                        self.in_degree[f"{block.name}.{attr.name}"] += 1

    def topological_sort(self):
        queue = deque()
        for block in self.blocks.values():
            for attr in block.attributes.values():
                full_name = f"{block.name}.{attr.name}"
                if self.in_degree[full_name] == 0:
                    queue.append(full_name)

        sorted_order = []
        while queue:
            current = queue.popleft()
            sorted_order.append(current)
            for neighbor in self.graph[current]:
                self.in_degree[neighbor] -= 1
                if self.in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return sorted_order

    def evaluate_formula(self, formula, local_env):
        try:
            return eval(formula, {}, local_env)
        except Exception as e:
            print(f"Error evaluating formula '{formula}': {e}")
            return None

    def evaluate_attribute(self, full_attr_name, name_map):
        attr = name_map[full_attr_name]
        if attr.type == "input":
            self.cache[full_attr_name] = attr.value
        elif attr.type == "calculated":
            local_env = {}
            for dep in attr.dependencies:
                if dep in self.cache:
                    local_env[dep.split(".")[1]] = self.cache[dep]
            result = self.evaluate_formula(attr.formula, local_env)
            self.cache[full_attr_name] = result
            attr.value = result

    def run_simulation(self):
        sorted_attributes = self.topological_sort()

        # Build a name to object map
        name_map = {}
        for block in self.blocks.values():
            for attr in block.attributes.values():
                name_map[f"{block.name}.{attr.name}"] = attr

        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(self.evaluate_attribute, full_attr_name, name_map)
                       for full_attr_name in sorted_attributes]
            for future in futures:
                future.result()  # Wait for all to complete
