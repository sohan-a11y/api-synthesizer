# Traffic-to-OpenAPI Synthesizer (`api-synthesizer`)

![GitHub License](https://img.shields.io/github/license/sohan-a11y/api-synthesizer?style=flat-square)
![GitHub Last Commit](https://img.shields.io/github/last-commit/sohan-a11y/api-synthesizer?style=flat-square)
![GitHub Stars](https://img.shields.io/github/stars/sohan-a11y/api-synthesizer?style=flat-square)
![GitHub Forks](https://img.shields.io/github/forks/sohan-a11y/api-synthesizer?style=flat-square)

[![Skills](https://skillicons.dev/icons?i=python,fastapi,git)](https://skillicons.dev)


A smart local mitmproxy addon that listens to your manual web browser interactions and automatically synthesizes a fully typed OpenAPI 3.0 YAML specification.

## Usage

1. Install requirements:
```bash
pip install -r requirements.txt
```

2. Start mitmproxy with the synthesizer addon:
```bash
mitmdump -s proxy.py
```

3. Configure your local browser proxy settings to point to `127.0.0.1:8080`.

4. Browse your target web application. As you perform fetch/XHR calls, the addon automatically parameterizes path IDs and infers request/response JSON schemas.

5. Press `Ctrl+C` to stop mitmproxy. The full OpenAPI specification will be saved to `generated_openapi.yaml`.