# FastAPI Journey

Tracking my FastAPI learning journey with hands-on projects, experiments, and progress notes as I build backend APIs step by step.

## About This Repository

This repository is my personal learning space where I document my progress in:
- FastAPI
- Docker
- API development best practices
- Deployment (including AWS)

I am using this repo to practice by building projects, trying new concepts, and improving my backend development skills over time.

## What I’m Learning

### FastAPI
- Routes and path/query parameters
- Request/response models with Pydantic
- Validation and error handling
- CRUD APIs
- Dependency injection
- Authentication and authorization
- Async APIs
- Testing FastAPI applications

### Docker
- Docker basics
- Writing Dockerfiles
- Containerizing FastAPI apps
- Running multi-service apps

### Deployment / DevOps
- Deploying FastAPI applications
- AWS deployment basics
- Environment variables and production setup

## Learning Source

I am also learning from the **CampusX FastAPI series** and related tutorials (including Docker and deployment topics).

## Repository Structure

```bash
FastAPI/
├── app/                # Main FastAPI application code
├── projects/           # Practice mini-projects / experiments
├── notes/              # Learning notes
├── tests/              # Test cases
├── requirements.txt    # Python dependencies
└── README.md
```

> The structure may change as I progress and organize things better.

## Progress Tracker

- [x] Git initialized and GitHub repo created
- [x] Build first FastAPI app
- [x] Add request validation with Pydantic
- [x] Create CRUD API
- [ ] Dockerize a FastAPI project
- [ ] Deploy a FastAPI app
- [ ] Learn AWS deployment basics
- [ ] Add tests

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/DaniManas/FastAPI.git
cd FastAPI
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

For Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI app

```bash
uvicorn app.main:app --reload
```

## Why This Repo?

This repository helps me:
- Track my learning progress
- Practice consistently
- Build small projects and experiments
- Revisit concepts later
- See my improvement over time

## Note

This is a learning repository, so code structure and quality will improve as I learn more and build better projects.
