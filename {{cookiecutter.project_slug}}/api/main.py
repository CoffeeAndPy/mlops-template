"""
{{cookiecutter.project_name}} API.

Included endpoints in this template:
GET /health     → liveness probe (Kubernetes / Docker Healtcheck).
GET /info       → Proyect information.
POST /predict   → placeholder - replace with real model

"""

import random
import logging
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("api")

# Model
# Global variable to hold the model instance
# It will load the model at startup and keep it in memory for subsequent requests.
model: Any = None

def load_model():
    """Load the model in memory."""
    global model
    # placeholder - replace with real model loading code.
    # model = joblib.load("model/model.pkl ")  # Example    
    model = {"type": "placeholder"}
    logger.info("Model loaded successfully.")

# Lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Starting up the API...")
    load_model()
    yield

    # Shutdown
    logger.info("Shutting down the API...")

app = FastAPI(
    title="{{cookiecutter.project_name}} API",
    description="API for {{cookiecutter.project_name}} model predictions.",
    version="0.1.0",
    lifespan=lifespan
)

# Schemas
class  PredictRequest(BaseModel):
    """Schema for prediction request."""
    value: float = Field(
        ..., 
        description="Input value for prediction",
        templates=42.0
        )
    
class PredictResponse(BaseModel):
    prediction: float
    model_version: str

# Endpoints

@app.get("/health")
def health():
    """
    Liveness probe endpoint.
    Returns 503 if the model is not loaded.
    """
    if model is None:
        # HTTPException will return de correct status code and message.
        raise HTTPException(status_code=503, detail="Model not loaded")
    return {"status": "ok", "model_loaded": True}

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