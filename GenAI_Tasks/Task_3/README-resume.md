# AI Resume Screening System with LangChain & LangSmith Tracing

A GenAI pipeline that screens resumes against a job description using LangChain (LCEL), Hugging Face, and LangSmith tracing.

---

## What It Does

Takes a resume + job description as input, then runs a 4-step pipeline:

```
Resume → Skill Extraction → Matching → Scoring → Explanation → Tracing
```

Outputs a fit score (0–100) with a reasoned explanation for each candidate.

---

## Project Structure

```
ai-resume-screening/
├── Task3_AI_Resume_screening.ipynb   # main notebook (all code)
└── README.md
```

The notebook is organized into modular sections that map to:
- `prompts/` — cells 4 (Prompts)
- `chains/` — cell 5 (Chains)
- `main.py` equivalent — cells 6–8 (Pipeline + Run + Summary)

---

## Setup

### 1. Open in Google Colab

Upload `Task_3_AI_Resume_screening.ipynb` to [colab.research.google.com](https://colab.research.google.com) or click **File → Open notebook → Upload**.

### 2. Get API Keys

| Key | Where to get it |
|-----|----------------|
| `HuggingFace_API_KEY` |
| `LANGCHAIN_API_KEY` |

### 3. Add Keys to Cell 2

```python
os.environ["HuggingFace_API_KEY"] = "sk-..."
os.environ["LANGCHAIN_API_KEY"] = "ls__..."
```

### 4. Run All Cells

`Runtime → Run all`

---

## Pipeline Steps

| Step | What happens |
|------|-------------|
| Skill Extraction | LLM reads the resume and pulls out skills, experience, tools, education |
| Matching | Extracted profile is compared against the job description |
| Scoring | LLM assigns a 0–100 fit score based on the match |
| Explanation | LLM explains why the score was given |

---

## Candidates Included

- **Strong** — 4 years experience, Python/ML/NLP/cloud stack, matches most requirements
- **Average** — 1.5 years, some Python/SQL, partial match
- **Weak** — 6-month IT internship, minimal relevant skills

---

## LangSmith Tracing

Tracing is enabled via:

```python
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "ai-resume-screening"
```

After running the notebook, go to [smith.langchain.com](https://smith.langchain.com) → your project → you'll see **3+ runs** with all pipeline steps visible.

Cell 10 includes a **deliberately bad prompt** to demonstrate debugging in LangSmith.

---

## Bonus Features Included

- Structured JSON output (Cell 9) with `fit_score`, `matched_skills`, `missing_skills`, and `recommendation`
- Debug run with intentional bad prompt (Cell 10) for LangSmith debugging demo

---

## Dependencies

```
langchain
langchain-openai
langsmith
python-dotenv
```

All installed automatically via Cell 1.

---

## Evaluation Criteria Coverage

| Criteria | Where |
|----------|-------|
| Pipeline Design | Cells 3–6 |
| LangChain Implementation | Cells 4–5 (PromptTemplate, LCEL, `.invoke()`) |
| Scoring & Logic | Cell 4 (scoring prompt with 0–100 guide) |
| Explainability | Cell 4 (explanation in scoring prompt) |
| LangSmith Tracing | Cell 2 + all `.invoke()` calls |
| Code Quality | Clean, minimal comments, modular cells |
| Bonus | Cells 9–10 (JSON output + debug case) |
