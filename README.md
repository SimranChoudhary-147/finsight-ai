# finsight-ai
A RAG-powered personal finance assistant that answers questions using real Indian financial documents, built in public, phase by phase.

💡 What is FinSight AI?
Ask it questions like:

"What is the current repo rate set by RBI?"
"Explain the expense ratio of HDFC Flexi Cap Fund"
"What are SEBI's rules on mutual fund NFOs?"

It answers using real public documents — RBI circulars, SEBI guidelines, AMFI factsheets, NSE/BSE filings — not hallucinated knowledge.

🏗️ Architecture
User Query
    │
    ▼
[ React Frontend ]
    │  HTTP
    ▼
[ FastAPI Backend ]
    │
    ├──► [ Embedding Model (OpenAI / Gemini) ]
    │
    ├──► [ ChromaDB Vector Store ] ──► Top-K Relevant Chunks
    │
    └──► [ LLM (GPT-4o / Gemini Pro) ] ──► Answer + Sources

📦 Tech Stack
LayerTechnologyBackendPython 3.11, FastAPIRAG FrameworkLangChain / LlamaIndexVector StoreChromaDB (local) → Pinecone (cloud)EmbeddingsOpenAI text-embedding-3-smallLLMGPT-4o-mini / Gemini ProFrontendReact 18, TailwindCSSContainerizationDocker, Docker ComposeCI/CDGitHub ActionsDeploymentRender (free tier)

🗺️ Build Roadmap
This project is built incrementally — one phase at a time, documented publicly.
PhaseWhatStatus✅ Phase 0Project setup, README, repo structureDone🔄 Phase 1Document ingestion + embedding pipelineIn Progress⏳ Phase 2RAG pipeline — retrieval + LLM generationUpcoming⏳ Phase 3React chat UI + conversation memoryUpcoming⏳ Phase 4Docker + GitHub Actions CI/CD + live deployUpcoming⏳ Phase 5Retrospective + v2 planningUpcoming

📂 Project Structure
finsight-ai/
│
├── backend/
│   ├── main.py                  # FastAPI app entry point
│   ├── ingest.py                # Document loading + embedding pipeline
│   ├── retriever.py             # Vector store query logic
│   ├── chain.py                 # RAG chain — retrieval + generation
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── components/
│   │   │   ├── ChatWindow.jsx
│   │   │   ├── MessageBubble.jsx
│   │   │   └── SourceCard.jsx
│   │   └── index.css
│   ├── package.json
│   └── Dockerfile
│
├── documents/                   # Public financial PDFs go here
│   ├── rbi/
│   ├── sebi/
│   └── amfi/
│
├── .github/
│   └── workflows/
│       └── deploy.yml           # CI/CD pipeline
│
├── docker-compose.yml
└── README.md

🚀 Getting Started (Phase 1 — local setup)
Prerequisites

Python 3.11+
Node.js 18+
An OpenAI API key (or Gemini API key)

1. Clone the repo
bashgit clone https://github.com/YOUR_USERNAME/finsight-ai.git
cd finsight-ai
2. Set up the backend
bashcd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
3. Add your API key
bashcp .env.example .env
# Edit .env and add: OPENAI_API_KEY=your_key_here
4. Add documents
Drop public PDF documents into the documents/ folder. Good starting sources:

RBI Circulars
SEBI Guidelines
AMFI Factsheets

5. Ingest documents
bashpython ingest.py
6. Run the backend
bashuvicorn main:app --reload
# API running at http://localhost:8000
7. Run the frontend
bashcd ../frontend
npm install
npm run dev
# App running at http://localhost:5173

📝 Build Journal (LinkedIn Posts)
Following along? Each phase has a post:

🔗 Phase 0 — Why I'm building this in public (posted)
Phase 1 — What I learned about document chunking (coming soon)
Phase 2 — RAG is harder than it looks (coming soon)
Phase 3 — Building the chat UI (coming soon)
Phase 4 — CI/CD and the Docker mistake that cost me 2 hours (coming soon)
Phase 5 — Full retrospective (coming soon)


📄 Documents Used
All documents used in this project are publicly available from official Indian regulatory and financial sources:

Reserve Bank of India (RBI) — public circulars
Securities and Exchange Board of India (SEBI) — public guidelines
AMFI India — publicly available mutual fund factsheets
NSE/BSE — publicly available filings

No proprietary or confidential data is used.

🤝 Contributing
This is a learning project built in public. If you spot something wrong or have ideas, open an issue — I'd love the input.

📬 Connect
Built by Simran Choudhary — Full Stack Developer II at BNY, building AI systems in fintech.
Follow the journey on LinkedIn for weekly updates.

