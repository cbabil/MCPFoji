import httpx
from fastmcp import FastMCP
from lib.args import parse_args
from lib.logger import setup_logging
import logging
import yaml
from urllib.parse import urljoin
from jsonref import JsonRef

def yaml_loader(uri):
    """Custom loader for jsonref to handle YAML files."""
    response = httpx.get(uri)
    response.raise_for_status()
    return yaml.safe_load(response.text)

def load_openapi_spec(spec_url: str) -> dict:
    """Loads an OpenAPI spec from a URL, resolving external references."""
    logging.info("Fetching spec from %s", spec_url)
    
    # Load the root spec
    base_spec = yaml_loader(spec_url)

    # Resolve external references, using the spec's URL as the base for relative refs
    resolved_spec = JsonRef.replace_refs(base_spec, base_uri=spec_url, loader=yaml_loader)
    
    return resolved_spec

def run_server(args):
    """Initializes and runs the FastMCP server."""
    logging.info("Creating HTTP client for API at %s", args.base_url)
    # Create an HTTP client for the API
    client = httpx.AsyncClient(base_url=args.base_url)

    # Load the OpenAPI spec
    try:
        logging.info("Loading OpenAPI spec from %s", args.spec_url)
        openapi_spec = load_openapi_spec(args.spec_url)
    except Exception as e:
        logging.error("Error loading spec: %s", e)
        exit(1)

    # Create the MCP server
    logging.info("Creating FastMCP server from OpenAPI spec")
    mcp = FastMCP.from_openapi(
        openapi_spec=openapi_spec,
        client=client,
        name="MCPFoji"
    )

    logging.info("Starting server with transport: %s", args.transport)
    if args.transport in ["http", "sse"]:
        mcp.run(
            transport=args.transport,
            host=args.host,
            port=args.port
        )
    else:
        mcp.run(transport=args.transport)

def main():
    """Main entry point of the script."""
    setup_logging()
    args = parse_args()
    run_server(args)

if __name__ == "__main__":
    main()
