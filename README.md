<div align="center">

# IndraGPT

**The open-source API layer that turns local models into production AI applications.**

</div>

---

Running a model locally is only the first step. To build useful AI applications you need a set of higher-level building blocks. **IndraGPT** provides that layer as an open-source API following the modern AI API models — so you can build private AI products without rebuilding the same backend primitives from scratch, and without depending on cloud APIs.

```text
Your app / agent / workflow / UI
              |
         IndraGPT API
              |
OpenAI-compatible inference server (Ollama, llama.cpp, vLLM, …)              
```

> IndraGPT does **not** run models itself. It connects to any OpenAI-compatible inference server via `OPENAI_API_BASE`. If it implements `/v1/chat/completions` and `/v1/models`, it works.

IndraGPT ships a built-in workbench UI for testing and demos, available at `/ui`. The API is the actual product.

---

## What IndraGPT gives you

- Standard messages API (streaming, async, token counting)
- File and artifact ingestion
- Retrieval with citations and agentic RAG
- Built-in tools (web search, web fetch, code execution)
- Custom tools and MCP connectors
- Structured access to databases and CSVs
- Embeddings and orchestration

---

## Quickstart

**Prerequisites:** You need a running OpenAI-compatible LLM server. Ollama is the easiest starting point.

**1. Install IndraGPT**

```bash
# Linux / macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

uv tool install --python 3.11 "indra-gpt[core]"
```

```powershell
# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

uv tool install --python 3.11 "indra-gpt[core]"
```

**2. Start your LLM server**

```bash
# Example with Ollama
ollama pull qwen3.5:35b         # LLM
ollama pull mxbai-embed-large   # Embeddings
ollama serve
```

**3. Run IndraGPT**

```bash
# macOS / Linux
OPENAI_API_BASE=http://localhost:<llm-port>/v1 \
  OPENAI_EMBEDDING_API_BASE=http://localhost:<embedding-port>/v1 \
  indra-gpt serve
```

```powershell
# Windows (PowerShell)
$env:OPENAI_API_BASE = "http://localhost:<llm-port>/v1"
$env:OPENAI_EMBEDDING_API_BASE = "http://localhost:<embedding-port>/v1"
indra-gpt serve
```

**4. Open the UI**

Go to [http://localhost:8080/ui](http://localhost:8080/ui). 

The UI is useful for:
- Sending messages.
- Selecting models from /v1/models.
- Uploading documents.
- Testing retrieval with citations.
- Enabling tools per chat.
- Configuring databases, MCP connectors, skills, and custom tools.
- Inspecting requests and responses through the API Debugger. 

This UI is a demonstrator, not the core product. Developers are expected to build their own applications on top of the API. 

---

## Community and contributing

Pull requests are welcome. Feel free to open issues for bug reports and feature requests.
