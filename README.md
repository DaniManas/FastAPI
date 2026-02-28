# FastAPI Journey

Tracking my FastAPI learning journey with hands-on projects, experiments, and progress notes as I build backend APIs step by step.

## About This Repository

This repository is my personal learning space where I document my progress in:
- FastAPI
- Docker
- API development best practices
- Deployment (including AWS)

I am using this repo to practice by building projects, trying new concepts, and improving my backend development skills over time.

## Featured Project Update

### Insurance Premium Prediction API

I built an end-to-end Insurance Premium Prediction API project and added it to this repository as part of my FastAPI learning journey.

What this project currently includes:
- Dockerized API with a production-ready `Dockerfile`
- Docker Hub image published: `manasadani/insurance-premium-api:latest`
- Trained ML model exported as `model.pkl`
- FastAPI prediction endpoint (`POST /predict`)
- Pydantic input validation
- Feature engineering inside the API flow (BMI, age group, lifestyle risk, city tier)
- Modular project structure (`config/`, `schema/`, `model/`)

Project path:
- `projects/insurance-premium-api/`

Data flow presentation:
- [📊 View Data Flow Presentation](https://danimanas.github.io/FastAPI/projects/insurance-premium-api/data_flow.html)

This project demonstrates my end-to-end workflow for building, containerizing, and deploying ML-backed APIs with FastAPI.


## Live Deployment

- Interactive Web App (Streamlit): [Open App](http://18.117.168.71:8501)
- Public API Base URL: `http://18.117.168.71:8000`
- Swagger Docs: `http://18.117.168.71:8000/docs`

## Current Repository Structure

```bash
FastAPI/
├── projects/
│   └── insurance-premium-api/   # ML model + FastAPI endpoint project
├── app.py / frontend.py / notebooks (older experiments)
├── requirements.txt
└── README.md
```

> The structure will keep evolving as I build more projects.

## Progress Tracker

- [x] Git initialized and GitHub repo created
- [x] Build first FastAPI app
- [x] Add request validation with Pydantic
- [x] Build ML model prediction endpoint with FastAPI
- [x] Complete insurance premium prediction API project
- [x] Dockerize the insurance premium API
- [x] Publish Docker image to Docker Hub
- [x] Deploy a FastAPI app
- [x] Learn AWS deployment basics
- [ ] Add tests

## Why This Repo?

This repository helps me:
- Track my learning progress
- Practice consistently
- Build small projects and experiments
- Revisit concepts later
- See my improvement over time

## Note

This is a learning repository, so code structure and quality will improve as I learn more and build better projects.
