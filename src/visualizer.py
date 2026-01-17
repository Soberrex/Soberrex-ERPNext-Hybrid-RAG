import os

class MermaidVisualizer:
    @staticmethod
    def generate(chunks, output_path="generated/workflow.mmd"):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        graph = ["graph TD"]
        for chunk in chunks:
            for call in chunk['calls']:
                if call not in ['print', 'len', 'str', 'int', 'dict']:
                    graph.append(f"    {chunk['name']} --> {call}")
        
        with open(output_path, "w") as f:
            f.write("\n".join(list(set(graph))))
        return output_path