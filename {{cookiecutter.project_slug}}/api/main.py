"""
{{cookiecutter.project_name}} API.

Included endpoints in this template:
GET /health     → liveness probe (Kubernetes / Docker Healtcheck).
GET /info       → Proyect information.
POST /predict   → placeholder - replace with real model

"""

import random
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    """Liveness probe endpoint."""
    return {"status": "ok"}

@app.get("/info")
def info():
    """Project information endpoint."""
    return {
        "project": "{{cookiecutter.project_name}}",
        "version": "0.1.0"
    }

@app.post("/predict")
def predict(body: dict):
    # accept any JSON body.
    return {"prediction": round(random.uniform(0, 1), 4)}