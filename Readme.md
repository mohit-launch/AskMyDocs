# 📚 AskMyDocs V1.0

> *"I read your PDFs so you don't have to. You're welcome."*

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
[![LangChain](https://img.shields.io/badge/🦜🔗_LangChain-Docs-blue.svg)](https://python.langchain.com/docs/get_started/introduction)
[![GitHub stars](https://img.shields.io/github/stars/mohit-launch/askmydocs.svg?style=social&label=Star&t=1)](https://github.com/mohit-launch/askmydocs)
[![GitHub issues](https://img.shields.io/github/issues/mohit-launch/askmydocs.svg)](https://github.com/mohit-launch/askmydocs/issues)
[![License](https://img.shields.io/github/license/mohit-launch/askmydocs.svg)](https://github.com/mohit-launch/askmydocs/blob/main/LICENSE)

AskMyDocs is a delightfully straightforward RAG (Retrieval-Augmented Generation) application that lets you interrogate your PDF documents. Toss your PDFs into a folder, ask questions, and get answers based **strictly** on what's in your docs. No hallucinations, no made-up nonsense, just the facts as written.

---

## 🛠️ The Tech Stack

This project is built on a modern, lightweight RAG stack:

* **Language:** Python 3.9+
* **LLM (The Brain):** Google Gemini Pro (via the Gemini API)
* **Embeddings (The Math):** `all-MiniLM-L6-v2` (SentenceTransformers) - Turns your text into high-dimensional vectors locally.
* **Vector Database (The Memory):** ChromaDB - Runs locally, persists your document embeddings so you don't have to re-process them every time.
* **Interface:** Custom-built Python CLI using `argparse`.

---

## 🏗️ Project Architecture

```text
AskMyDocs/
├── main.py              # The CLI entry point (ingest & ask)
├── __init__.py          # The glue holding this beautiful mess together
├── processor.py         # PDF loader & text chunker
├── embedding.py         # Handles the MiniLM embedding logic
├── vector_store.py      # ChromaDB config - where document memories live
├── llm_handler.py       # Talks to Gemini and formats your sassy prompts
├── requirements.txt     # Python dependencies
└── data/                # [Create this] Your PDFs go here
```

---

## 🚀 Quick Start

### 1. Clone & Install
Get the code and install the dependencies. 

```bash
git clone [https://github.com/mohit-launch/AskMyDocs.git](https://github.com/yourusername/AskMyDocs.git)
cd AskMyDocs
pip install -r requirements.txt
```

### 2. Get Your API Key
* Head over to Google AI Studio.
* Click "Get API Key".
* Copy that shiny string of characters.

### 3. Set Your Secret Sauce
Create a `.env` file in the root of the project and drop your key in:

```bash
GEMINI_API_KEY=your_super_secret_key_here
```
> **Note:** No quotes. No spaces. Just `KEY=value` exactly like nature intended.

### 4. Feed the Machine
Create a folder called `data/` in the root directory and dump your PDFs in there. 

---

## 💻 CLI Usage

We built a clean CLI so you don't have to write any extra code to use this. 

### Step 1: Ingest your documents
Run this to slice your PDFs and build the vector database. You only need to do this once, or whenever you add new PDFs to the folder.
```bash
python main.py ingest
```
*(Custom folders? Keep your PDFs somewhere else? Use the dir flag: `python main.py ingest --dir /path/to/pdfs`)*

### Step 2: Interrogate your documents
Wrap your question in quotes and ask away:
```bash
python main.py ask "What does the document say about the new policy?"
```

*(Forget the commands? Just run `python main.py -h` for the help menu).*

---

 🧠 How It Actually Works

1. **Chop:** Loads your PDFs and slices them into tiny, digestible text chunks.
2. **Mathify:** Embeds each chunk into a numerical vector.
3. **Store:** Saves those vectors in ChromaDB for lightning-fast retrieval.
4. **Fetch & Answer:** You ask a question -> it finds the most mathematically similar chunks -> feeds them to Gemini -> returns a human-readable answer.

---

## 💡 Pro Tips

* **Patience is a virtue:** The very first time you run `ingest`, it will download the embedding model (~80MB). Grab a coffee. It only happens once.
* **Don't repeat yourself:** The vector store is persisted locally in a `vectorstore/` folder. Skip `ingest` on future runs unless you've added new PDFs.

---

## 🚨 Troubleshooting

| Problem | Likely Solution |
| :--- | :--- |
| **`GEMINI_API_KEY not found`** | Did you make the `.env` file? Are you sure it's not named `.env.txt`? Did you spell it right? |
| **No PDFs found** | Did you actually put PDFs in the `data/` folder? Are they actually `.pdf` files? |
| **Vector store is empty** | You need to run `python main.py ingest` at least once. |

---

## 📜 License

MIT License is used 

---
*Made with ☕ and mild frustration.*
```
