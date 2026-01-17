import ast

class DependencyTracker(ast.NodeVisitor):
    def __init__(self):
        self.calls = []
        
    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            self.calls.append(node.func.id)
        elif isinstance(node.func, ast.Attribute):
            self.calls.append(node.func.attr)
        self.generic_visit(node)

class CodeParser:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tree = ast.parse(source_code)

    def extract_chunks(self):
        chunks = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                tracker = DependencyTracker()
                tracker.visit(node)
                source = ast.get_source_segment(self.source_code, node)
                chunks.append({
                    "name": node.name,
                    "code": source,
                    "calls": list(set(tracker.calls))
                })
        return chunks