# ArgoAgent

<div align="center">
  <img src="./pics/logo.png" alt="Logo" width="200">
  <h1 align="center">ArgoAgent</h1>
  <h2 align="center">A vessel not of wood, but of discovery</h2>

</div>
<div align="center">
<!-- Keep these links. Translations will automatically update with the README. -->
  
[Deutsch](https://zdoc.app/de/BV003/ArgoAgent) | 
[English](https://zdoc.app/en/BV003/ArgoAgent) | 
[Español](https://zdoc.app/es/BV003/ArgoAgent) | 
[français](https://zdoc.app/fr/BV003/ArgoAgent) | 
[日本語](https://zdoc.app/ja/BV003/ArgoAgent) | 
[한국어](https://zdoc.app/ko/BV003/ArgoAgent) | 
[Português](https://zdoc.app/pt/BV003/ArgoAgent) | 
[Русский](https://zdoc.app/ru/BV003/ArgoAgent) | 
[中文](https://zdoc.app/zh/BV003/ArgoAgent)

</div>


### 🚀 Introduction
核心目标是构建一个通用的 agent 包，让开发者能方便地创建和扩展智能代理


### ✨ Features
#### Intelligent Interaction with Context Preservation
Automatically determines whether to call external tools or generate direct LLM responses based on user instructions, while maintaining context throughout the interaction.


### 🌐 Environment



### 📂 Project Structure

```
├── src
│   ├── argoagent
│   │   ├── __init__.py
│   │   ├── agent
│   │   │   └── agent.py
│   │   ├── cli
│   │   ├── context
│   │   │   └── context.py
│   │   ├── llm
│   │   │   ├── __init__.py
│   │   │   ├── base_llm.py
│   │   │   ├── doubao_llm.py
│   │   │   └── openai_llm.py
│   │   ├── log
│   │   ├── tools
│   │   │   ├── base.py
│   │   │   ├── builtins
│   │   │   │   ├── echo.py
│   │   │   │   └── fetch.py
│   │   │   ├── file
│   │   │   ├── registry.py
│   │   │   └── web
│   │   ├── utils
│   │   └── workflows
│   │       │   
│   │       ├── base.py
│   │       ├── human_in_loop.py
│   │       ├── loop.py
│   │       ├── parallel.py
│   │       ├── router.py
│   │       └── single_step.py

    
```

```mermaid
classDiagram
    class Agent {
        +init(),初始化方法，连接 MCP 服务器并加载工具，创建 LLM 实例。
        +close(),关闭所有 MCP 客户端连接。
        +invoke(prompt: string),核心方法，接收用户输入，协调 LLM 与工具调用，处理循环工具调用逻辑，返回最终结果。
        
        -mcpClients: MCPClient[],存储多个 MCP 客户端实例，用于工具调用。
        -llm: ChatOpenAI,ChatOpenAI 实例，负责与大语言模型交互。
        -model: string,使用的大语言模型名称
        -systemPrompt: string,系统提示词，用于初始化模型行为。
        -context: string,注入模型的上下文信息（如 RAG 检索结果）
    }
    class ChatOpenAI {
        +chat(prompt?: string),与 LLM 对话的核心方法，支持传入用户提示，返回模型响应（包含文本内容和工具调用信息），支持流式输出。
        +appendToolResult(toolCallId: string, toolOutput: string),将工具调用结果追加到对话历史，供模型后续处理。

        getToolsDefinition()：将 MCP 工具转换为 OpenAI 工具调用格式。

        -llm: OpenAI,OpenAI 官方 SDK 实例，用于调用 API。
        -model: string,使用的大语言模型名称。
        -messages: OpenAI.Chat.ChatCompletionMessageParam[],存储对话历史消息（包括用户输入、模型输出、工具调用结果）。
        -tools: Tool[],可用的工具列表（从 MCP 客户端获取）。

    }
    class EmbeddingRetriever {
        +embedDocument(document: string) 将文档转换为向量嵌入并存储到向量库。
        +embedQuery(query: string) 将用户查询转换为向量嵌入。
        +retrieve(query: string, topK: number) 根据查询向量从向量库中检索最相关的 topK 个文档。
        -embeddingModel: string ,使用的嵌入模型名称（如 BAAI/bge-m3）
        -vectorStore: VectorStore ,向量存储实例，用于存储和检索文档嵌入。
    }
    class MCPClient {
        +init()
        +close()
        +getTools()
        +callTool(name: string, params: Record<string, any>)
        -mcp: Client
        -command: string
        -args: string[]
        -transport: StdioClientTransport
        -tools: Tool[]
    }
    class VectorStore {
        +addEmbedding(embedding: number[], document: string)将向量嵌入与对应文档添加到存储中
        +search(queryEmbedding: number[], topK: number)计算查询向量与存储中所有向量的余弦相似度，返回最相似的 topK 个文档。
        -vectorStore: VectorStoreItem[] 存储向量嵌入及对应文档的列表。
    }
    class VectorStoreItem {
        -embedding: number[] 文档的向量嵌入。
        -document: string 嵌入对应的原始文档内容。
    }

    Agent --> MCPClient : uses
    Agent --> ChatOpenAI : interacts with
    ChatOpenAI --> ToolCall : manages
    EmbeddingRetriever --> VectorStore : uses
    VectorStore --> VectorStoreItem : contains
```

### ⚡ Quick Start
- 

### 🎯 Core Tech


### 🤝 Contributing

We welcome contributions! Whether it's:

- Bug fixes
- New features
- Documentation improvements
- Translations

Please:  
- Check existing issues first  
- Open an issue to discuss major changes  
- Submit PRs with clear descriptions  



### 🔥 For Beginners

**This is an independent educational project, designed for learning and practice.**

If you are new to open source:
- Don’t worry! This project is meant to be beginner-friendly 
- You can start small (update README, add comments, fix small bugs) 
- You can build on top of this project, customize it, and even use it as part of your course assignments or personal practice projects.🤪


### 🎉 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### 🙏 Acknowledgments
This project draws inspiration from and builds upon the following projects:
- [mcp-agent](https://github.com/lastmile-ai/mcp-agent) 
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) 
- [llm-mcp-rag](https://github.com/KelvinQiu802/llm-mcp-rag)
- [Building effective agents by Anthropic](https://www.anthropic.com/engineering/building-effective-agents)✅
- [A video about Prompt, Agent, MCP](https://www.bilibili.com/video/BV1aeLqzUE6L/?spm_id_from=333.788.recommend_more_video.0&vd_source=6710a28cdc7d2834e160d5fb90681095)✅
- [MCP SDK(python)](https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file#fastmcp-properties)✅