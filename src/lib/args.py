import argparse

def parse_args():
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(
        description="""
        A FastMCP server that dynamically generates tools from a Swagger/OpenAPI
        specification.

        Run this script with a URL to a spec file to start the server.
        Example:
            python main.py --spec-url http://your-api.com/openapi.json --transport http
        """,
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "--spec-url",
        required=True,
        help="The URL of the Swagger/OpenAPI specification."
    )
    parser.add_argument(
        "--transport",
        default="stdio",
        choices=["stdio", "http", "sse"],
        help="The transport to use."
    )
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="The host to bind to for http and sse transports."
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="The port to use for http and sse transports."
    )
    parser.add_argument(
        "--base-url",
        default="http://localhost:9990",
        help="The base URL for the API being wrapped."
    )
    return parser.parse_args()
