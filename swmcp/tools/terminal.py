"""Terminal operation tools."""

from typing import Optional
from fastmcp import FastMCP


def register(mcp: FastMCP) -> None:
    """Register terminal tools.
    
    Args:
        mcp: FastMCP server instance
    """
    
    @mcp.tool()
    async def execute_command(
        command: str,
        cwd: Optional[str] = None,
        timeout: int = 30
    ) -> dict:
        """Execute a shell command and return output.
        
        Args:
            command: Command to execute
            cwd: Working directory (optional)
            timeout: Timeout in seconds
            
        Returns:
            Dictionary with stdout, stderr, and exit code
        """
        # TODO: Implement using Rust extension for performance
        raise NotImplementedError("Terminal execution not yet implemented")
    
    @mcp.tool()
    async def ssh_connect(
        host: str,
        port: int = 22,
        username: Optional[str] = None,
        key_path: Optional[str] = None
    ) -> dict:
        """Establish SSH connection to remote host.
        
        Args:
            host: Remote hostname or IP
            port: SSH port
            username: SSH username
            key_path: Path to private key file
            
        Returns:
            Connection status and session ID
        """
        # TODO: Implement using Rust asyncssh
        raise NotImplementedError("SSH connection not yet implemented")
