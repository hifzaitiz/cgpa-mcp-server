import os

from fastmcp import FastMCP
from tools import tools

mcp = FastMCP("cgpa")

for tool in tools:
    mcp.tool(tool)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    mcp.run(transport="http", host="0.0.0.0", port=port)
