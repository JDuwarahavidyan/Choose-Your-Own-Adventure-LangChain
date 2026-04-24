<div align="center">

# 📖 AI Story Forge

### *Generate immersive, branching adventure stories powered by AI*

<br/>

![React](https://img.shields.io/badge/React_19-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI_GPT--4o-412991?style=for-the-badge&logo=openai&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![Python](https://img.shields.io/badge/Python_3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)

<br/>

> **Choose your path. Shape your destiny. Every theme becomes an epic.**

</div>

---

## ✨ What is AI Story Forge?

**AI Story Forge** is a full-stack, AI-powered interactive storytelling platform. You provide a theme — *fantasy*, *sci-fi*, *mystery*, anything* — and GPT-4o generates a rich, branching narrative with multiple choices, paths, and endings. Navigate the story by making decisions and see where your choices lead.

No two playthroughs are ever the same.

---

## 🎮 How It Works

```
You enter a theme  ──►  AI generates the full story tree  ──►  You play through it
       │                        │                                      │
  "Space pirate"          Branching nodes,                   Click choices,
                          win/loss endings,                  uncover endings,
                          multiple paths                     replay differently
```

1. **Enter a theme** on the home screen
2. The backend **queues an async generation job** and returns a job ID instantly
3. The frontend **polls every 5 seconds** until the story is ready
4. You are dropped into the **interactive story interface**
5. Click choices to **navigate the narrative tree**
6. Reach a **win or loss ending** — or try again from the start

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        Frontend                              │
│  React 19  ·  React Router  ·  Axios  ·  Vite               │
│                                                             │
│  StoryGenerator  ──►  ThemeInput  ──►  LoadingStatus        │
│       │                                     │               │
│  StoryLoader  ──────────────────────►  StoryGame            │
└────────────────────────┬────────────────────────────────────┘
                         │  HTTP / REST
┌────────────────────────▼────────────────────────────────────┐
│                        Backend                               │
│  FastAPI  ·  Uvicorn  ·  LangChain  ·  SQLAlchemy           │
│                                                             │
│  POST /api/stories/create                                   │
│  GET  /api/jobs/{job_id}          ◄── polling               │
│  GET  /api/stories/{id}/complete                            │
└────────────────────────┬────────────────────────────────────┘
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
       SQLite /       OpenAI        LangChain
      PostgreSQL      GPT-4o        Chains
```

---

## 🧰 Tech Stack

### 🖥️ Frontend

| Technology | Purpose |
|---|---|
| ⚛️ **React 19** | UI library and component model |
| 🛣️ **React Router DOM 7** | Client-side page routing |
| ⚡ **Vite 8** | Lightning-fast dev server and build tool |
| 🌐 **Axios** | API communication with the backend |

### ⚙️ Backend

| Technology | Purpose |
|---|---|
| 🚀 **FastAPI** | High-performance async REST API |
| 🦜 **LangChain + LangChain OpenAI** | LLM orchestration and chain management |
| 🤖 **OpenAI GPT-4o mini** | AI story generation engine |
| 🗄️ **SQLAlchemy 2.0** | ORM for database abstraction |
| 🔍 **Pydantic** | Data validation and settings management |
| 🦄 **Uvicorn** | ASGI production server |

### 🗃️ Database

| Mode | Details |
|---|---|
| 🧪 **Development** | SQLite (zero-config, file-based) |
| 🏭 **Production** | PostgreSQL via `DATABASE_URL` env variable |

### 📦 DevOps

| Technology | Purpose |
|---|---|
| 🐳 **Docker** | Backend containerisation |
| 🎼 **Docker Compose** | Multi-service orchestration |
| ☁️ **Choreo** | Cloud deployment platform |

---

## 📁 Project Structure

```
📦 Full Stack Project
├── 🖥️ frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── StoryGenerator.jsx    # Home page: theme input + job polling
│   │   │   ├── StoryGame.jsx         # Interactive story navigation UI
│   │   │   ├── StoryLoader.jsx       # Fetches complete story by ID
│   │   │   ├── ThemeInput.jsx        # Form component for theme entry
│   │   │   └── LoadingStatus.jsx     # Animated loading indicator
│   │   ├── App.jsx                   # Router configuration
│   │   ├── main.jsx                  # React entry point
│   │   └── util.js                   # API base URL constant
│   ├── vite.config.js                # Vite config with dev proxy
│   └── package.json
│
└── ⚙️ backend/
    ├── core/
    │   ├── config.py                 # Pydantic settings loader
    │   ├── models.py                 # Pydantic models for LLM output
    │   ├── prompts.py                # System prompt for story generation
    │   └── story_generator.py        # LangChain + OpenAI integration
    ├── db/
    │   └── database.py               # SQLAlchemy engine and session
    ├── models/
    │   ├── story.py                  # Story and StoryNode ORM models
    │   └── job.py                    # StoryJob ORM model
    ├── schemas/
    │   ├── story.py                  # API response schemas
    │   └── job.py                    # Job status schemas
    ├── routers/
    │   ├── story.py                  # Story creation and retrieval routes
    │   └── job.py                    # Job polling route
    ├── main.py                       # FastAPI application entry point
    ├── Dockerfile
    ├── compose.yaml
    └── requirements.txt
```

---

## 🗄️ Database Schema

```
┌──────────────────┐        ┌───────────────────────┐
│     stories      │        │      story_nodes       │
├──────────────────┤        ├───────────────────────┤
│ id (PK)          │◄──┐    │ id (PK)               │
│ title            │   └────│ story_id (FK)          │
│ session_id       │        │ content               │
│ created_at       │        │ is_root               │
└──────────────────┘        │ is_ending             │
                            │ is_winning_ending     │
                            │ options (JSON)        │
                            └───────────────────────┘

┌───────────────────────────────┐
│          story_jobs           │
├───────────────────────────────┤
│ id (PK)                       │
│ job_id (UUID, unique)         │
│ session_id                    │
│ theme                         │
│ status  (pending/processing/  │
│          completed/failed)    │
│ story_id (FK, nullable)       │
│ error (nullable)              │
│ created_at / completed_at     │
└───────────────────────────────┘
```

---

## 🚀 Getting Started

### Prerequisites

- 🟢 **Node.js** 18+ and npm
- 🐍 **Python** 3.11+
- 🔑 An **OpenAI API key**
- 🐳 **Docker** (optional, for containerised runs)

---

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/JDuwarahavidyan/ai-story-forge.git
cd ai-story-forge
```

### 2️⃣ Backend Setup

```bash
cd backend

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

**`.env` file:**
```env
OPENAI_API_KEY=your_openai_api_key_here
DATABASE_URL=sqlite:///./database.db
API_PREFIX=/api
DEBUG=True
ALLOW_ORIGINS=http://localhost:5173
```

```bash
# Start the backend server
uvicorn main:app --reload --port 8000
```

### 3️⃣ Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start the development server
npm run dev
```

Open [http://localhost:5173](http://localhost:5173) in your browser.

---

### 🐳 Docker Setup (Recommended)

```bash
cd backend

# Build and run with Docker Compose
docker compose up --build
```

The API will be available at `http://localhost:8000`.

---

## 🌐 API Reference

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/stories/create` | Submit a theme and create a story generation job |
| `GET` | `/api/jobs/{job_id}` | Poll job status (pending / processing / completed / failed) |
| `GET` | `/api/stories/{story_id}/complete` | Retrieve the full story tree |
| `GET` | `/api/stories/health` | Stories router health check |
| `GET` | `/api/jobs/health` | Jobs router health check |

### Example: Create a Story

```bash
curl -X POST http://localhost:8000/api/stories/create \
  -H "Content-Type: application/json" \
  -d '{"theme": "space pirate adventure"}'
```

```json
{
  "job_id": "3f7a9b2c-1234-5678-abcd-ef0123456789",
  "status": "pending",
  "story_id": null
}
```

---

## 🔄 Async Story Generation Flow

```
Client                    FastAPI                  Background Task
  │                          │                           │
  │── POST /stories/create ──►│                           │
  │                          │── spawn task ─────────────►│
  │◄── { job_id, "pending" }──│                           │── call OpenAI
  │                          │                           │── parse story tree
  │── GET /jobs/{job_id} ────►│                           │── persist to DB
  │◄── { status: "processing" }                          │
  │                          │                           │
  │── GET /jobs/{job_id} ────►│◄── update to "completed" ─│
  │◄── { status: "completed", story_id: 42 }             │
  │                          │                           │
  │── GET /stories/42/complete►│                          │
  │◄── { root_node, all_nodes }                          │
```

---

## ☁️ Deployment

This project is configured for deployment on **[Choreo](https://choreo.dev/)** via `.choreo/component.yaml`.

```yaml
# .choreo/component.yaml
endpoints:
  - name: backend
    port: 8000
    type: REST
    visibility: Public
```

For other platforms, the `Dockerfile` is ready to use as-is. Set the `DATABASE_URL` environment variable to a PostgreSQL connection string for production persistence.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">

Built with ❤️ by **Duwarahavidyan J**

⭐ *If you find this project interesting, give it a star!* ⭐

</div>
