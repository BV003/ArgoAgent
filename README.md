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
ArgoAgent is designed to implement a basic intelligent agent without relying on any heavy frameworks.
Its goal is to demonstrate the core functionality of an agent—receiving a task, accessing tools, reasoning, and producing output—while keeping the system lightweight and easy to understand.


### ✨ Features
- Custom Tools — Easily add or define your own tools for the agent to interact with.
- RAG Enhancement — Integrate retrieval-augmented generation to improve agent reasoning with external knowledge.
- Context Logging — Keep detailed logs of agent interactions and context for debugging and analysis.
- Workflow Support — Define multi-step tasks and orchestrate complex workflows.
- Multi-Model Compatibility — Supports different language models, making the agent flexible for various use cases.


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
    class Workflow {
        agent
        run()
    }

    class Agent {
        name
        llm
        tool_registry
        log_context
        retrieved_context

        run_single_step()
        parse_llm_response()
    }

    class BaseLLM {
        api_key
        generate()
    }

    class LogContext {
        history
        add_message()
        print_history()
        save_to_file()
    }


    class ToolRegistry {
        tools
        get()
        list_tools()
    }

    class Tool {
        name
        description
        parameters
        run()
    }

    class EmbeddingRetriever {
        model
        vector_store
        embed_document()
        embed_query()
        _embed()
        retrieve()
    }

    class VectorStore {
        vector_store
        add_embedding()
        search()
    }

    class VectorStoreRetriever {
        embedding
        document
    }

    Workflow --> Agent
    Agent --> BaseLLM
    Agent --> LogContext
    Agent --> ToolRegistry
    Agent --> EmbeddingRetriever
    ToolRegistry --> Tool
    EmbeddingRetriever --> VectorStore
    VectorStore --> VectorStoreRetriever
  ```

### ⚡ Quick Start
Clone the Repository
```
git clone https://github.com/BV003/ArgoAgent.git
cd ArgoAgent
```
Create and Activate Virtual Environment. We recommend using conda for dependency management.
```
conda create -n argo python=3.10 -y
conda activate argo
```
Install Dependencies
```
pip install -r requirements.txt
pip install -e .
```
Create a .env file in the project root directory and add your API Keys (e.g., OpenAI or other LLM providers) You can also use other models, as long as you implement the corresponding class under /llm.
```
OPENAI_API_KEY=your_api_key_here  //openai
ARK_API_KEY=your_api_key_here //doubao
```



### 🧪 Demo
#### test_log
run the code
```
python examples/test_log.py
```
the result is
```
**打印对话历史**
 User: 你好
 Assistant: 你好，有什么可以帮你？
 User: 帮我写一个测试脚本
 Assistant: 好的，已经写好啦！
=====================
```
#### test_rag
run the code
```
python examples/test_rag.py
```
the result is
```
--- Query ---
Which city, known for its art and the Eiffel Tower, serves as the capital of France?

--- Retrieved Documents ---
1. Paris, located on the River Seine, is the largest city and cultural hub of France.
2. Python is widely used for web development, data analysis, and AI research.
```
#### test_tool
run the code
```
python examples/test_tool.py
```
the result is
```
Available tools: [{'name': 'echo', 'description': 'Echo input text', 'parameters': {'text': '需要输出的文本内容（必填，字符串类型）'}}, {'name': 'fetch', 'description': 'Fetch content from a URL', 'parameters': {'url': '需要抓取的网页地址（必填，字符串类型，必须包含http/https协议）', 'max_length': '返回内容的最大长度（可选，整数类型，默认值为1000，超出部分会被截断）'}}, {'name': 'calculator', 'description': '执行数学计算，支持加减乘除、幂运算、三角函数等表达式', 'parameters': {'expression': "字符串，需要计算的数学表达式，例如 '123*456'、'sin(30°)'、'sqrt(16)'"}}]
[Calculator] Result: 56088
[Calculator] Result: 0.5
[Calculator] Result: 18
[Echo] Result: EchoTool: Hello MCP
[Fetch] Result: <!DOCTYPE html>
<!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charset=utf-8><meta http-equiv=X-UA-Compatible content=IE=Edge><meta content=always name=referrer><link re ...

--- Context History ---

**打印对话历史**
=====================
```
#### test_workflow
run the code
```
python examples/test_workflow.py
```
the result is
```
Available tools: [{'name': 'echo', 'description': 'Echo input text', 'parameters': {'text': '需要输出的文本内容（必填，字符串类型）'}}, {'name': 'fetch', 'description': 'Fetch content from a URL', 'parameters': {'url': '需要抓取的网页地址（必填，字符串类型，必须包含http/https协议）', 'max_length': '返回内容的最大长度（可选，整数类型，默认值为1000，超出部分会被截断）'}}]

[LoopWorkflow] Result: 任务已完成，无需进一步操作。
当前结果：EchoTool: 123乘以456的结果是56088
是否继续？(y/n) y

[HumanInLoopWorkflow] Result: 任务已完成，无需进一步操作。

[ParallelWorkflow] Results: ['Result of task1', 'Result of task2']

[RouterWorkflow] say_hello: Hello MCP
[RouterWorkflow] say_bye: Bye MCP
```
#### comprehensive_demo
run the code
```
python examples/comprehensive_demo.py
```
the result is
```
Available tools: [{'name': 'echo', 'description': 'Echo input text', 'parameters': {'text': '需要输出的文本内容（必填，字符串类型）'}}, {'name': 'fetch', 'description': 'Fetch content from a URL', 'parameters': {'url': '需要抓取的网页地址（必填，字符串类型，必须包含http/https协议）', 'max_length': '返回内容的最大长度（可选，整数类型，默认值为1000，超出部分会被截断）'}}]

[示例 1] Agent result: EchoTool: 请用 echo 工具输出一句话

[示例 2] Agent result: <!DOCTYPE html>
<!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charset=utf-8><meta http-equiv=X-UA-Compatible content=IE=Edge><meta content=always name=referrer><link rel=stylesheet type=text/css href=https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/bdorz/baidu.min.css><title>百度一下，你就知道</title></head> <body link=#0000cc> <div id=wrapper> <div id=head> <div class=head_wrapper> <div class=s_form> <div class=s_form_wrapper> <div id=lg> <img hidefocus=true src=//www.baidu.com/img/bd_logo1.png width=270 height=129> </div> <form id=form name=f action=//www.baidu.com/s class=fm> <input type=hidden name=bdorz_come value=1> <input type=hidden name=ie value=utf-8> <input type=hidden name=f value=8> <input type=hidden name=rsv_bp value=1> <input type=hidden name=rsv_idx value=1> <input type=hidden name=tn value=baidu><span class="bg s_ipt_wr"><input id=kw name=wd class=s_ipt value maxlength=255 autocomplete=off autofocus=autofocus></span><span class="bg s_bt...

[示例 3] Agent result: 任务已完成，无需进一步操作。

--- Context History ---
user: 请用 echo 工具输出一句话
llm: {"action": "call_tool", "name": "echo", "parameters": {"text": "请用 echo 工具输出一句话"}}
tool: 工具 echo 返回：EchoTool: 请用 echo 工具输出一句话
user: 帮我抓取 https://www.baidu.com 的内容
llm: {"action": "call_tool", "name": "fetch", "parameters": {"url": "https://www.baidu.com"}}
tool: 工具 fetch 返回：<!DOCTYPE html>
<!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charset=utf-8><meta http-equiv=X-UA-Compatible content=IE=Edge><meta content=always name=referrer><link rel=stylesheet type=text/css href=https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/bdorz/baidu.min.css><title>百度一下，你就知道</title></head> <body link=#0000cc> <div id=wrapper> <div id=head> <div class=head_wrapper> <div class=s_form> <div class=s_form_wrapper> <div id=lg> <img hidefocus=true src=//www.baidu.com/img/bd_logo1.png width=270 height=129> </div> <form id=form name=f action=//www.baidu.com/s class=fm> <input type=hidden name=bdorz_come value=1> <input type=hidden name=ie value=utf-8> <input type=hidden name=f value=8> <input type=hidden name=rsv_bp value=1> <input type=hidden name=rsv_idx value=1> <input type=hidden name=tn value=baidu><span class="bg s_ipt_wr"><input id=kw name=wd class=s_ipt value maxlength=255 autocomplete=off autofocus=autofocus></span><span class="bg s_bt...
user: 请使用 echo 工具和 fetch 工具，最后用 echo 工具输出百度首页的标题关键词
llm: {"action": "call_tool", "name": "fetch", "parameters": {"url": "https://www.baidu.com"}}
tool: 工具 fetch 返回：<!DOCTYPE html>
<!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charset=utf-8><meta http-equiv=X-UA-Compatible content=IE=Edge><meta content=always name=referrer><link rel=stylesheet type=text/css href=https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/bdorz/baidu.min.css><title>百度一下，你就知道</title></head> <body link=#0000cc> <div id=wrapper> <div id=head> <div class=head_wrapper> <div class=s_form> <div class=s_form_wrapper> <div id=lg> <img hidefocus=true src=//www.baidu.com/img/bd_logo1.png width=270 height=129> </div> <form id=form name=f action=//www.baidu.com/s class=fm> <input type=hidden name=bdorz_come value=1> <input type=hidden name=ie value=utf-8> <input type=hidden name=f value=8> <input type=hidden name=rsv_bp value=1> <input type=hidden name=rsv_idx value=1> <input type=hidden name=tn value=baidu><span class="bg s_ipt_wr"><input id=kw name=wd class=s_ipt value maxlength=255 autocomplete=off autofocus=autofocus></span><span class="bg s_bt...
user: 基于上一步结果，继续处理：<!DOCTYPE html>
<!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charset=utf-8><meta http-equiv=X-UA-Compatible content=IE=Edge><meta content=always name=referrer><link rel=stylesheet type=text/css href=https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/bdorz/baidu.min.css><title>百度一下，你就知道</title></head> <body link=#0000cc> <div id=wrapper> <div id=head> <div class=head_wrapper> <div class=s_form> <div class=s_form_wrapper> <div id=lg> <img hidefocus=true src=//www.baidu.com/img/bd_logo1.png width=270 height=129> </div> <form id=form name=f action=//www.baidu.com/s class=fm> <input type=hidden name=bdorz_come value=1> <input type=hidden name=ie value=utf-8> <input type=hidden name=f value=8> <input type=hidden name=rsv_bp value=1> <input type=hidden name=rsv_idx value=1> <input type=hidden name=tn value=baidu><span class="bg s_ipt_wr"><input id=kw name=wd class=s_ipt value maxlength=255 autocomplete=off autofocus=autofocus></span><span class="bg s_bt...
llm: {"action": "call_tool", "name": "echo", "parameters": {"text": "百度一下，你就知道"}}
任务已完成，无需进一步操作。
tool: 工具 echo 返回：EchoTool: 百度一下,你就知道
user: 基于上一步结果，继续处理：EchoTool: 百度一下,你就知道
llm: 任务已完成，无需进一步操作。
llm: 任务已完成，无需进一步操作。
```

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
- [Building effective agents by Anthropic](https://www.anthropic.com/engineering/building-effective-agents)
- [A video about Prompt, Agent, MCP](https://www.bilibili.com/video/BV1aeLqzUE6L/?spm_id_from=333.788.recommend_more_video.0&vd_source=6710a28cdc7d2834e160d5fb90681095)
- [MCP SDK(python)](https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file#fastmcp-properties)