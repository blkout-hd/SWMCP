"""CLI entry point."""

import typer
from swmcp.server import main as server_main
from swmcp.gui import main as gui_main

app = typer.Typer(
    name="swmcp",
    help="SWMCP - High-Performance MCP Server"
)


@app.command()
def server():
    """Start the MCP server."""
    server_main()


@app.command()
def gui():
    """Launch the observability GUI."""
    gui_main()


@app.command()
def version():
    """Show version information."""
    from swmcp import __version__
    typer.echo(f"SWMCP version {__version__}")


def main():
    """Main CLI entry point."""
    app()


if __name__ == "__main__":
    main()
