"""SWMCP - High-Performance MCP Server with Rust Extensions."""

__version__ = "0.1.0"
__author__ = "SBSCRPT Corp"
__license__ = "MIT"

from swmcp import server, tools, agents, auth, storage

__all__ = ["server", "tools", "agents", "auth", "storage", "__version__"]
