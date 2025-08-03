# MCPFoji

<p align="center">
  <img src="assets/mcpfoji.png" alt="MCPFoji Logo" width="200" height="200">
</p>

<p align="center">
  <strong>A MCP server that dynamically generates tools from Swagger/OpenAPI specifications</strong>
</p>

<p align="center">
  <a href="https://github.com/cbabil/MCPFoji/wiki">📖 Wiki</a> •
  <a href="https://github.com/cbabil/MCPFoji/issues">🐛 Issues</a> •
  <a href="https://github.com/cbabil/MCPFoji/discussions">💬 Discussions</a> •
  <a href="https://github.com/cbabil/MCPFoji/releases">🚀 Releases</a>
</p>

---

## 🌟 What is MCPFoji?

MCPFoji is a powerful Model Context Protocol (MCP) server that automatically generates tools from OpenAPI/Swagger specifications. It bridges the gap between API documentation and usable MCP tools, enabling AI assistants to interact with any API that has proper OpenAPI documentation.

## ✨ Features

- 🔄 **Dynamic Tool Generation**: Automatically creates MCP tools from OpenAPI specs
- 🌐 **Multiple Transports**: Supports stdio, HTTP, and Server-Sent Events (SSE)
- 📁 **External References**: Resolves external YAML references in OpenAPI specs
- 🔧 **Configurable**: Flexible configuration options for different deployment scenarios
- 🚀 **MCP Powered**: Built on the efficient MCP framework

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/cbabil/MCPFoji.git
   cd MCPFoji
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the server**
   ```bash
   python src/main.py --spec-url http://your-api.com/openapi.json
   ```

## 📖 Usage

### Basic Usage

```bash
# Start with stdio transport (default)
python src/main.py --spec-url http://your-api.com/openapi.json

# Start with HTTP transport
python src/main.py --spec-url http://your-api.com/openapi.json --transport http --port 8000

# Start with SSE transport
python src/main.py --spec-url http://your-api.com/openapi.json --transport sse --host 0.0.0.0 --port 8080
```

### Command Line Options

| Option | Default | Description |
|--------|---------|-------------|
| `--spec-url` | Required | URL of the Swagger/OpenAPI specification |
| `--transport` | `stdio` | Transport type: `stdio`, `http`, or `sse` |
| `--host` | `127.0.0.1` | Host to bind to (for http/sse transports) |
| `--port` | `8000` | Port to use (for http/sse transports) |
| `--base-url` | `http://localhost:9990` | Base URL for the API being wrapped |

### Examples

#### Example 1: Local API with HTTP Transport
```bash
python src/main.py \
  --spec-url http://localhost:9990/docs \
  --transport http \
  --base-url http://localhost:9990 \
  --port 8000
```

#### Example 2: Remote API with Default Transport
```bash
python src/main.py \
  --spec-url https://api.example.com/docs \
  --base-url https://api.example.com
```

## 🏗️ How It Works

1. **Spec Loading**: MCPFoji fetches the OpenAPI specification from the provided URL
2. **Reference Resolution**: External YAML references are automatically resolved
3. **Tool Generation**: Each API endpoint becomes an MCP tool with proper typing
4. **Server Start**: The MCP server starts with your chosen transport method

## 🔧 Configuration

MCPFoji supports various configuration options through command-line arguments. For more advanced configuration scenarios, please refer to the [Wiki](https://github.com/cbabil/MCPFoji/wiki).

## 📁 Project Structure

```
MCPFoji/
├── src/
│   ├── main.py           # Main application entry point
│   └── lib/
│       ├── args.py       # Command-line argument parsing
│       ├── logger.py     # Logging configuration
│       └── __init__.py
├── assets/
│   └── mcpfoji.png      # Project logo
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── LICENSE              # License information
└── Makefile             # Build automation
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](https://github.com/cbabil/MCPFoji/wiki/Contributing) for details.

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Run tests (if available)
5. Submit a pull request

## 📝 License

This project is licensed under the terms specified in the [LICENSE](LICENSE) file.

## 🔗 Related Projects

- [FastMCP](https://github.com/jlowin/fastmcp) - The underlying MCP framework
- [Model Context Protocol](https://modelcontextprotocol.io/) - Official MCP documentation

## 🆘 Support

- 📖 Check the [Wiki](https://github.com/cbabil/MCPFoji/wiki) for detailed documentation
- 🐛 Report bugs in [Issues](https://github.com/cbabil/MCPFoji/issues)
- 💬 Ask questions in [Discussions](https://github.com/cbabil/MCPFoji/discussions)
- 📧 Contact the maintainer: [@cbabil](https://github.com/cbabil)

## 🙏 Acknowledgments

- Thanks to the MCP team for providing the excellent MCP framework
- Inspired by the need for better API-to-MCP integration tools

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/cbabil">@cbabil</a>
</p>