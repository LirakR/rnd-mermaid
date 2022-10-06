import ast
from typing import Any, Dict

class Visitor(ast.NodeVisitor):
    models_schema: Dict[str, Any]

    def __init__(self):
        self.models_schema = {}

    def visit_ClassDef(self, node: ast.AST):
        fields = []
        if isinstance(node, ast.ClassDef):
            for item in node.body:
                if not isinstance(item, ast.AnnAssign):
                    continue
                field_type = ast.unparse(item.annotation)

                fields.append(
                    {
                        "field_name": item.target.id,
                        "field_type": field_type
                    }
                )
            self.models_schema[node.name] = {
                "parents": [parent.id for parent in node.bases],
                "fields": fields
            }
        self.generic_visit(node)
        return self.models_schema

def get_schema(path: str):
    with open(path) as f:
        code = f.read()

    node = ast.parse(code)
    visitor = Visitor()
    # visitor.models_schema = {}
    schema = visitor.visit_ClassDef(node)
    return schema


def generate_mermaid_class(name: str, data: Dict[str, Any]):
    fields = data["fields"]
    fields_str = ""
    for field in fields:
        fields_str += f"\t- {field['field_name']}: {field['field_type']}\n"

    return f"""class {name}{{\n{fields_str if fields_str else "..."}\n}}\n"""


def generate_mermaid_connections(name: str, data: Dict[str, Any]):
    connections = ""
    for parent in data["parents"]:
        connections += f"{name} --> {parent}\n"
    return connections


def generate_mermaid(schema: Dict[str, Any], direction: str):
    mermaid_classes = ""
    mermaid_connections = ""
    for key, val in schema.items():
        mermaid_classes +=generate_mermaid_class(key, val)
        mermaid_connections += generate_mermaid_connections(key, val)

    mermaid_final = f"""classDiagram\n\tdirection {direction}\n\t{mermaid_classes}{mermaid_connections}"""
    return mermaid_final

