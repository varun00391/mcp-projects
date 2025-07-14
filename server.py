# # server.py
# from fastmcp import FastMCP

# mcp = FastMCP("Demo")

# @mcp.tool
# def add(a: int, b: int) -> int:
#     """Add two numbers"""
#     return a + b

# if __name__ == "__main__":
#     mcp.run()

# my_server.py
from fastmcp import FastMCP
import asyncio # We'll need this later for the client

# Instantiate the server, giving it a name
mcp = FastMCP(name="My First MCP Server")

print("FastMCP server object created.")

if __name__ == "__main__":
    print("\n--- Starting FastMCP Server via __main__ ---")
    # This starts the server, typically using the stdio transport by default
    mcp.run()


# fastmcp run server.py
