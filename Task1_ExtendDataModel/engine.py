from collections import deque
from model import Attribute

class SimulationEngine:
    def __init__(self, blocks):
        self.blocks = blocks
        self.graph = {}
        self.eval_order = []

    def run_simulation(self):
        self.build_dependency_graph()
        self.topological_sort()
        self.evaluate_attributes()
        return self.blocks

    def build_dependency_graph(self):
        self.graph = {}

        for block_name, block in self.blocks.items():
            for attr in block.attributes.values():
                qualified_name = f"{block_name}.{attr.name}"
                if attr.type == "calculated":
                    self.graph[qualified_name] = []
                    for dep in attr.dependencies:
                        dep_block = self._find_block_by_attr(dep)
                        if dep_block:
                            dep_qualified = f"{dep_block}.{dep}"
                            if dep_qualified not in self.graph:
                                self.graph[dep_qualified] = []
                            self.graph[dep_qualified].append(qualified_name)

    def topological_sort(self):
        indegree = {node: 0 for node in self.graph}
        for deps in self.graph.values():
            for neighbor in deps:
                indegree[neighbor] += 1

        queue = deque([n for n in self.graph if indegree[n] == 0])
        sorted_nodes = []

        while queue:
            node = queue.popleft()
            sorted_nodes.append(node)
            for neighbor in self.graph.get(node, []):
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        self.eval_order = sorted_nodes

    def evaluate_attributes(self):
        context = self._build_context()

        for full_attr_name in self.eval_order:
            block_name, attr_name = full_attr_name.split(".")
            attr = self.blocks[block_name].attributes[attr_name]
            if attr.type == "calculated":
                try:
                    attr.value = eval(attr.formula, {}, context)
                    context[attr_name] = attr.value
                except Exception as e:
                    print(f"Failed to evaluate {attr_name}: {e}")

    def _qualified_name(self, attr: Attribute, block):
        return f"{block.name}.{attr.name}"

    def _build_context(self):
        context = {}
        for block in self.blocks.values():
            for attr in block.attributes.values():
                if attr.type == "input":
                    context[attr.name] = attr.value
        return context

    def _find_block_by_attr(self, attr_name):
        for block_name, block in self.blocks.items():
            if attr_name in block.attributes:
                return block_name
        return None
