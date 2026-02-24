# FastAPI Journey

Tracking my FastAPI learning journey with hands-on projects, experiments, and progress notes as I build backend APIs step by step.

## About This Repository

This repository is my personal learning space where I document my progress in:
- FastAPI
- Docker
- API development best practices
- Deployment (including AWS)

I am using this repo to practice by building projects, trying new concepts, and improving my backend development skills over time.

## Learning Source

I am learning from the **CampusX FastAPI series** and related tutorials (including Docker and deployment topics), and using this repo to track my implementations and improvements.

## Featured Project Update

### Insurance Premium Prediction API (Video Implementation)

I completed a FastAPI project based on the tutorial and added it to this repository as part of my learning journey.

What this project currently includes:
- Trained ML model exported as `model.pkl`
- FastAPI prediction endpoint (`POST /predict`)
- Pydantic input validation
- Feature engineering inside the API flow (BMI, age group, lifestyle risk, city tier)
- Modular project structure (`config/`, `schema/`, `model/`)

Project path:
- `projects/insurance-premium-api/`

This is my tutorial-based implementation that I will later improve with Dockerization, deployment, and a stronger real-world use case (like churn prediction).

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
- [x] Complete insurance premium prediction API project (tutorial-based)
- [ ] Dockerize the insurance premium API
- [ ] Deploy a FastAPI app
- [ ] Learn AWS deployment basics
- [ ] Add tests
- [ ] Build a stronger showcase project (e.g., churn prediction)

## Why This Repo?

This repository helps me:
- Track my learning progress
- Practice consistently
- Build small projects and experiments
- Revisit concepts later
- See my improvement over time

## Note

This is a learning repository, so code structure and quality will improve as I learn more and build better projects.
