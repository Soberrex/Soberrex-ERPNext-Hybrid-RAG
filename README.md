# 🏛️ ERPNext Architectural Refactoring Agent

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![AI](https://img.shields.io/badge/AI-Llama%203.2-meta)
![Status](https://img.shields.io/badge/Status-Prototype-orange)

**Internal Codename:** "The Architect"

## 🎯 The Core Problem
Legacy enterprise systems like **ERPNext** are massive and monolithic. Standard AI coding assistants fail when working with them because they treat code as plain text. They guess variable names and hallucinate dependencies because they lack **structural context**.

**The Solution:** This project implements a **Hybrid Graph-RAG Architecture** that combines semantic search with Abstract Syntax Tree (AST) analysis to deterministically refactor legacy code.

## 🚀 Key Features (The "Secret Sauce")

### 1. Hybrid Retrieval Engine ("The Sniper")
Unlike basic RAG tools that rely solely on vector similarity, this agent uses a dual-path approach:
* **Dense Search (ChromaDB):** Uses local embeddings (`all-MiniLM-L6-v2`) to find conceptual matches.
* **Sparse Search (BM25):** Uses exact keyword matching to pinpoint specific function names or error codes.
* **Neural Re-Ranking:** A Cross-Encoder (`ms-marco-MiniLM-L-6-v2`) acts as a "Judge," re-scoring the top 20 results to eliminate 95% of noise.

### 2. Structural Intelligence
Once the target file is found, the agent does not just read it.
* **AST Parsing:** It parses the Python Abstract Syntax Tree to map the call graph.
* **Dependency Injection:** It feeds *only* the relevant function context to the LLM, preventing context-window overflow.

### 3. Agentic Refactoring
* **Engine:** Powered by **Llama 3.2 (3B)** via OpenRouter for cost-effective, high-speed reasoning.
* **Action:** Automatically extracts monolithic logic into clean **Service Layers** adhering to the Single Responsibility Principle.
* **Verification:** Auto-generates **Pytest** unit tests to ensure the new code is reliable.

---

## 🛠️ Tech Stack

| Component | Technology | Reasoning |
| :--- | :--- | :--- |
| **Orchestration** | Python 3.12+ | Standard for AI Engineering. |
| **Vector DB** | `chromadb` | Lightweight, local semantic storage. |
| **Embeddings** | `sentence-transformers` | **Local Model** (Zero latency, $0 cost, No Rate Limits). |
| **Re-Ranking** | `cross-encoder` | Increases retrieval accuracy by ~40%. |
| **Intelligence** | **Llama 3.2** (via OpenRouter) | State-of-the-art reasoning at low cost. |
| **Graphing** | `networkx` | For dependency mapping and visualization. |
| **Visualization** | `mermaid.js` | Generates flowcharts of the refactoring path. |

---

## 📂 Project Structure

```text
ERPNext-Analyzer/
├── .env                        # Configuration & API Keys (OpenRouter)
├── main.py                     # CLI Entry Point
├── project_context.md          # Project documentation & context
├── requirements.txt            # Python dependencies
├── chroma_db/                  # Persistent Vector Database storage
├── data/                       # Raw data & BM25 sparse indices
├── generated/                  # 📂 Output Folder (AI Results)
│   ├── new_service.py          # Refactored Service Class (AI Output)
│   ├── test_service.py         # Auto-generated Unit Tests
│   └── workflow.mmd            # Dependency Graph Diagram
└── src/                        # 🧠 Core Source Code
    ├── __init__.py             # Package initializer
    ├── indexer.py              # Hybrid Search Engine (Local Embeddings + BM25)
    ├── parser.py               # Abstract Syntax Tree (AST) Parser
    ├── pipeline_manager.py     # Manages the Parser -> Visualizer -> AI workflow
    ├── refactoring_engine.py   # AI Agent (Llama 3.2 via OpenRouter)
    └── visualizer.py           # Diagram Generator

    Here is the fully updated, professional version of your Project Bible (which you should save as README.md for GitHub).

I have updated the Tech Stack, File Structure, and Narrative to match your recent changes (switching to Llama 3.2, Local Embeddings, and the new file names like pipeline_manager.py).

📝 Action: Create/Overwrite README.md
Copy and paste the code block below into a file named README.md in your project folder.

Markdown

# 🏛️ ERPNext Architectural Refactoring Agent

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![AI](https://img.shields.io/badge/AI-Llama%203.2-meta)
![Status](https://img.shields.io/badge/Status-Prototype-orange)

**Internal Codename:** "The Architect"

## 🎯 The Core Problem
Legacy enterprise systems like **ERPNext** are massive and monolithic. Standard AI coding assistants fail when working with them because they treat code as plain text. They guess variable names and hallucinate dependencies because they lack **structural context**.

**The Solution:** This project implements a **Hybrid Graph-RAG Architecture** that combines semantic search with Abstract Syntax Tree (AST) analysis to deterministically refactor legacy code.

## 🚀 Key Features (The "Secret Sauce")

### 1. Hybrid Retrieval Engine ("The Sniper")
Unlike basic RAG tools that rely solely on vector similarity, this agent uses a dual-path approach:
* **Dense Search (ChromaDB):** Uses local embeddings (`all-MiniLM-L6-v2`) to find conceptual matches.
* **Sparse Search (BM25):** Uses exact keyword matching to pinpoint specific function names or error codes.
* **Neural Re-Ranking:** A Cross-Encoder (`ms-marco-MiniLM-L-6-v2`) acts as a "Judge," re-scoring the top 20 results to eliminate 95% of noise.

### 2. Structural Intelligence
Once the target file is found, the agent does not just read it.
* **AST Parsing:** It parses the Python Abstract Syntax Tree to map the call graph.
* **Dependency Injection:** It feeds *only* the relevant function context to the LLM, preventing context-window overflow.

### 3. Agentic Refactoring
* **Engine:** Powered by **Llama 3.2 (3B)** via OpenRouter for cost-effective, high-speed reasoning.
* **Action:** Automatically extracts monolithic logic into clean **Service Layers** adhering to the Single Responsibility Principle.
* **Verification:** Auto-generates **Pytest** unit tests to ensure the new code is reliable.

---

## 🛠️ Tech Stack

| Component | Technology | Reasoning |
| :--- | :--- | :--- |
| **Orchestration** | Python 3.12+ | Standard for AI Engineering. |
| **Vector DB** | `chromadb` | Lightweight, local semantic storage. |
| **Embeddings** | `sentence-transformers` | **Local Model** (Zero latency, $0 cost, No Rate Limits). |
| **Re-Ranking** | `cross-encoder` | Increases retrieval accuracy by ~40%. |
| **Intelligence** | **Llama 3.2** (via OpenRouter) | State-of-the-art reasoning at low cost. |
| **Graphing** | `networkx` | For dependency mapping and visualization. |
| **Visualization** | `mermaid.js` | Generates flowcharts of the refactoring path. |

---

## 📂 Project Structure

```text
ERPNext-Analyzer/
├── main.py                     # CLI Entry Point
├── requirements.txt            # Dependency list
├── .env                        # API Keys (OPENROUTER_API_KEY)
├── data/                       # Local ChromaDB & BM25 indices
├── generated/                  # AI Outputs (Refactored Code, Diagrams)
└── src/
    ├── __init__.py
    ├── indexer.py              # Hybrid Search Engine (Local Embeddings)
    ├── pipeline_manager.py     # The "Brain" (Orchestrates Search -> Refactor)
    ├── parser.py               # AST Code Analyzer
    ├── refactoring_engine.py   # Llama 3.2 Interface
    └── visualizer.py           # Mermaid Diagram Generator


⚡ Quick Start
1. Installation
Clone the repository and install the dependencies.

Bash
pip install -r requirements.txt

2. Configuration
Create a .env file and add your OpenRouter key:

Ini, TOML

OPENROUTER_API_KEY=sk-or-v1-...
3. Initialize the Brain
Scan your dataset to build the Vector and Keyword indices.

Bash

python main.py init data/
4. Run the Agent
Ask a question to trigger the pipeline (Search -> Analyze -> Refactor).

Bash

python main.py ask "How are taxes calculated?"
📊 Pipeline Visualized
User Query: "Refactor the tax logic."

Hybrid Indexer: Retrieves sales_invoice.py (Rank 1).

AST Parser: Identifies calculate_taxes_and_totals is the root cause.

Llama 3.2 Agent: Writes SalesTaxService class.

Output: Saves new_service.py and test_service.py.

📜 License
MIT License. Built for the Open Source Community.