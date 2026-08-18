import json
from mitmproxy import http
from schema_builder import OpenAPIGenerator

class APISynthesizerAddon:
    def __init__(self):
        self.generator = OpenAPIGenerator()

    def response(self, flow: http.HTTPFlow):
        # Filter for JSON responses
        content_type = flow.response.headers.get("content-type", "")
        if "application/json" not in content_type:
            return

        method = flow.request.method
        full_url = flow.request.url
        query_params = dict(flow.request.query)

        req_body = None
        if flow.request.text:
            try:
                req_body = json.loads(flow.request.text)
            except Exception:
                pass

        res_status = flow.response.status_code
        res_body = None
        if flow.response.text:
            try:
                res_body = json.loads(flow.response.text)
            except Exception:
                pass

        print(f"[API Synthesizer] Captured: {method} {full_url}")
        self.generator.add_interaction(
            method=method,
            full_url=full_url,
            query_params=query_params,
            req_body=req_body,
            res_status=res_status,
            res_body=res_body
        )

    def done(self):
        print("[API Synthesizer] Mitmproxy shutting down. Exporting generated_openapi.yaml...")
        self.generator.export_yaml("generated_openapi.yaml")

addons = [APISynthesizerAddon()]
