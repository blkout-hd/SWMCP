"""Tool registration for FastMCP server."""

from fastmcp import FastMCP
from swmcp.tools import terminal, files, process


def register_tools(mcp: FastMCP) -> None:
    """Register all MCP tools with the server.
    
    Args:
        mcp: FastMCP server instance
    """
    # Terminal tools
    terminal.register(mcp)
    
    # File operation tools
    files.register(mcp)
    
    # Process management tools
    process.register(mcp)
