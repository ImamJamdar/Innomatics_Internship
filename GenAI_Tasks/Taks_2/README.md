# LangChain: Deep Technical Blog — Code Examples

**Author:** Imam  
**Internship:** Data Science Intern @ Innomatics Research Labs  
**Blog:** [Read the full blog on Medium](https://medium.com/@imamsab.im22/langchain-ffcb16610c92)

---

## About

This repository contains all working Python code examples from the blog post **"LangChain: The Framework That Finally Makes LLMs Actually Useful"**.

Every notebook cell maps directly to a concept explained in the blog — from a basic LLM call all the way to autonomous agents with tools.

---

## What's Inside

| Notebook Section | Concept Covered |
|---|---|
| Basic LLM Call | ChatOpenAI with system + human messages |
| Prompt Templates | ChatPromptTemplate with dynamic variables |
| Chains (LCEL) | Pipe syntax: `prompt \| llm \| parser` |
| Memory | Multi-turn conversation with MessagesPlaceholder |
| RAG Pipeline | TextLoader → FAISS → RetrievalQA |
| Agents & Tools | Custom tools with `@tool` + AgentExecutor |

---

## How to Run

**1. Clone the repo**
```bash
git clone https://github.com/your-username/langchain-blog.git
cd langchain-blog
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Add your API key**

Open `langchain_demo.ipynb` and replace:
```python
os.environ["OPENAI_API_KEY"] = "your-openai-api-key-here"
```

**4. Launch the notebook**
```bash
jupyter notebook langchain_demo.ipynb
```

---

## Requirements

```
langchain
langchain-openai
langchain-community
faiss-cpu
openai
```

---

## Blog & References

- 📖 Full Blog: https://medium.com/@imamsab.im22/langchain-ffcb16610c92
- 🔗 LangChain Docs: https://python.langchain.com
- 🔗 LangChain GitHub: https://github.com/langchain-ai/langchain

---

*Data Science Internship — Innomatics Research Labs — February 2026*
