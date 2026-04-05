"""Main FastMCP server implementation."""

import asyncio
import os
from typing import Optional

from fastmcp import FastMCP
from swmcp.tools import register_tools
from swmcp.auth import setup_auth
from swmcp.storage import setup_storage


def create_server(name: str = "SWMCP") -> FastMCP:
    """Create and configure the FastMCP server instance.
    
    Args:
        name: Server name for MCP protocol
        
    Returns:
        Configured FastMCP server instance
    """
    mcp = FastMCP(name)
    
    # Register all tools
    register_tools(mcp)
    
    # Setup authentication if configured
    auth_mode = os.getenv("AUTH_MODE", "tpm")
    if auth_mode:
        setup_auth(mcp, mode=auth_mode)
    
    # Setup storage backend
    storage = setup_storage()
    mcp.context["storage"] = storage
    
    return mcp


def main() -> None:
    """Run the MCP server."""
    server = create_server()
    asyncio.run(server.run())


if __name__ == "__main__":
    main()
