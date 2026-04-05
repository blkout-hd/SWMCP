"""Tests for FastMCP server."""

import pytest
from swmcp.server import create_server


def test_server_creation():
    """Test server can be created."""
    server = create_server()
    assert server is not None
    assert server.name == "SWMCP"


def test_server_has_tools(mcp_server):
    """Test server has registered tools."""
    # TODO: Verify tools are registered
    pass
