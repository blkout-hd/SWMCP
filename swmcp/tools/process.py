"""Process management tools."""

from typing import Optional, List
from fastmcp import FastMCP


def register(mcp: FastMCP) -> None:
    """Register process management tools.
    
    Args:
        mcp: FastMCP server instance
    """
    
    @mcp.tool()
    async def list_processes(
        filter_pattern: Optional[str] = None
    ) -> List[dict]:
        """List running processes.
        
        Args:
            filter_pattern: Optional name filter
            
        Returns:
            List of process information dictionaries
        """
        # TODO: Implement using psutil
        raise NotImplementedError("Process listing not yet implemented")
    
    @mcp.tool()
    async def kill_process(
        pid: int,
        signal: int = 15
    ) -> dict:
        """Send signal to process.
        
        Args:
            pid: Process ID
            signal: Signal number (default SIGTERM)
            
        Returns:
            Status dictionary
        """
        # TODO: Implement process signal handling
        raise NotImplementedError("Process kill not yet implemented")
