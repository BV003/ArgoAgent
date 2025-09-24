import asyncio
from pathlib import Path
from argoagent.tools.mcp_client import MCPClient

async def main():
    # out_path = str(Path("/home/lwq_0/Argo/ArgoAgent/temp"))
    # Path(out_path).mkdir(parents=True, exist_ok=True)

    # 初始化 MCP 客户端
    fetch_mcp = MCPClient("mcp-server-fetch", ["mcp-server-fetch"], "uvx")
    # file_mcp = MCPClient("mcp-server-file", ["-y", "@modelcontextprotocol/server-filesystem", out_path], "npx")
    
    await fetch_mcp.init()
    # await file_mcp.init()
    
    print("Fetch MCP Tools:", fetch_mcp.get_tools())
    # print("File MCP Tools:", file_mcp.get_tools())




    # 调用 fetch 工具
    print("\nCalling tool fetch on fetch MCP...")
    fetch_result = await fetch_mcp.call_tool(
        "fetch",
        {"url": "https://www.baidu.com", "max_length": 5000}
    )
    print("Fetch Result:", fetch_result)

    调用 file MCP 的 read_text_file 工具示例
    example_file = str(Path(out_path) / "example.txt")
    # 写入一个示例文件
    await file_mcp.call_tool("write_file", {"path": example_file, "content": "Hello MCP! I am testing file read and write."})
    # 读取文件内容
    read_result = await file_mcp.call_tool("read_text_file", {"path": example_file})
    print("\nRead file Result:", read_result)


    #     # 安全关闭 MCP 客户端
    await fetch_mcp.close()
    await file_mcp.close()


if __name__ == "__main__":
    asyncio.run(main())
