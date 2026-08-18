# Traffic-to-OpenAPI Synthesizer ⚡

![GitHub License](https://img.shields.io/github/license/sohan-a11y/api-synthesizer?style=flat-square)
![GitHub Last Commit](https://img.shields.io/github/last-commit/sohan-a11y/api-synthesizer?style=flat-square)
![GitHub Stars](https://img.shields.io/github/stars/sohan-a11y/api-synthesizer?style=flat-square)
![GitHub Forks](https://img.shields.io/github/forks/sohan-a11y/api-synthesizer?style=flat-square)


Traffic-to-OpenAPI Synthesizer: Automatic path parameterization and JSON schema inference from live HTTP traffic.

---

## 🌟 Key Features

- ⚡ **Real-time Traffic Sniffing**: Integrated mitmproxy addon captures HTTP/HTTPS requests on the fly.
- 🧩 **Dynamic Schema Inference**: Automatically extracts request/response JSON structures and types.
- 🛣️ **Path Parameterization**: Identifies RESTful path IDs (`/users/123` -> `/users/{id}`).
- 📄 **OpenAPI 3.0 Generation**: Outputs valid YAML/JSON OpenAPI specifications instantly.

---

## 🛠️ Tech Stack

[![Skills](https://skillicons.dev/icons?i=python,fastapi,git)](https://skillicons.dev)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+ / Node.js (depending on module)
- Git

### Installation
```bash
# Clone repository
git clone https://github.com/sohan-a11y/api-synthesizer.git
cd api-synthesizer

# Install dependencies (if python project)
pip install -r requirements.txt
```

---

## 💡 Usage Example

```bash
# Run application entrypoint
python main.py
```

---

## 🗺️ Roadmap & Future Enhancements
- [x] Initial release & core functionality
- [ ] Enterprise security integration
- [ ] Multi-tenant Cloud deployment support
- [ ] Advanced performance profiling

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to check the [issues page](https://github.com/sohan-a11y/api-synthesizer/issues).

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for details.
