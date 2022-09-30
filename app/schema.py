import ast

class Visitor(ast.NodeVisitor):
    models_schema = {}

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
    schema = Visitor().visit_ClassDef(node)
    return schema



if __name__ == "__main__":
    schema = get_schema("bi3_models/bi3_scrapers_api/models.py")
    breakpoint()
    ...
