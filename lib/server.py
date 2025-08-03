import httpx
from fastmcp import FastMCP
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def run_server(args):
    """Initializes and runs the FastMCP server."""
    logging.info("Creating HTTP client for API at %s", args.base_url)
    # Create an HTTP client for the API
    client = httpx.AsyncClient(base_url=args.base_url)

    # Load the OpenAPI spec
    try:
        logging.info("Loading OpenAPI spec from %s", args.spec_url)
        openapi_spec = httpx.get(args.spec_url).json()
    except Exception as e:
        logging.error("Error loading spec: %s", e)
        exit(1)

    # Create the MCP server
    logging.info("Creating FastMCP server from OpenAPI spec")
    mcp = FastMCP.from_openapi(
        openapi_spec=openapi_spec,
        client=client,
        name="SwaggerMCP"
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
