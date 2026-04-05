"""Pytest configuration and fixtures."""

import pytest
from swmcp.server import create_server


@pytest.fixture
def mcp_server():
    """Create test MCP server instance."""
    return create_server(name="SWMCP-Test")


@pytest.fixture
def temp_file(tmp_path):
    """Create temporary file for testing."""
    test_file = tmp_path / "test.txt"
    test_file.write_text("test content\n")
    return test_file
