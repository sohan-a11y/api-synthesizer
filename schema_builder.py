from typing import Any
from ruamel.yaml import YAML
from path_normalizer import normalize_path

class OpenAPIGenerator:
    def __init__(self, title: str = "Synthesized Web App API", version: str = "1.0.0"):
        self.spec: dict[str, Any] = {
            "openapi": "3.0.3",
            "info": {
                "title": title,
                "version": version,
                "description": "Auto-generated OpenAPI spec from captured network traffic."
            },
            "paths": {}
        }

    def infer_json_schema(self, data: Any) -> dict:
        if data is None:
            return {"type": "string", "nullable": True}
        elif isinstance(data, bool):
            return {"type": "boolean"}
        elif isinstance(data, int):
            return {"type": "integer"}
        elif isinstance(data, float):
            return {"type": "number"}
        elif isinstance(data, str):
            return {"type": "string"}
        elif isinstance(data, list):
            if not data:
                return {"type": "array", "items": {}}
            item_schemas = [self.infer_json_schema(item) for item in data]
            return {"type": "array", "items": item_schemas[0]}
        elif isinstance(data, dict):
            properties = {}
            for key, val in data.items():
                properties[key] = self.infer_json_schema(val)
            return {"type": "object", "properties": properties}
        return {"type": "string"}

    def add_interaction(self, method: str, full_url: str, query_params: dict, req_body: Any | None, res_status: int, res_body: Any | None):
        norm_path, path_params = normalize_path(full_url)
        method_lower = method.lower()

        if norm_path not in self.spec["paths"]:
            self.spec["paths"][norm_path] = {}

        parameters = []
        for p_name, p_type in path_params.items():
            parameters.append({
                "name": p_name,
                "in": "path",
                "required": True,
                "schema": {"type": "integer" if "integer" in p_type else "string"}
            })
        for q_name, q_val in query_params.items():
            parameters.append({
                "name": q_name,
                "in": "query",
                "required": False,
                "schema": self.infer_json_schema(q_val)
            })

        operation: dict[str, Any] = {
            "summary": f"{method.upper()} {norm_path}",
            "parameters": parameters,
            "responses": {}
        }

        if req_body:
            operation["requestBody"] = {
                "content": {
                    "application/json": {
                        "schema": self.infer_json_schema(req_body)
                    }
                }
            }

        status_str = str(res_status)
        response_obj: dict[str, Any] = {"description": f"Status {res_status} response"}
        if res_body:
            response_obj["content"] = {
                "application/json": {
                    "schema": self.infer_json_schema(res_body)
                }
            }
        operation["responses"][status_str] = response_obj

        self.spec["paths"][norm_path][method_lower] = operation

    def export_yaml(self, filepath: str = "generated_openapi.yaml"):
        yaml = YAML()
        yaml.default_flow_style = False
        with open(filepath, "w", encoding="utf-8") as f:
            yaml.dump(self.spec, f)
