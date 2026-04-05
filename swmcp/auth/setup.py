"""Authentication setup and configuration."""

from fastmcp import FastMCP


def setup_auth(mcp: FastMCP, mode: str = "tpm") -> None:
    """Setup authentication for the server.
    
    Args:
        mcp: FastMCP server instance
        mode: Authentication mode ('tpm' or 'rsa-hmac')
    """
    if mode == "tpm":
        # TODO: Setup TPM-based authentication
        pass
    elif mode == "rsa-hmac":
        # TODO: Setup RSA-HMAC authentication
        pass
    else:
        raise ValueError(f"Unknown auth mode: {mode}")
