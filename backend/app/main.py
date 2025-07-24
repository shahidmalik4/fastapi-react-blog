from fastapi import FastAPI
from app import models, database
from app.routes import router

# Create tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(router)

# In backend/app/main.py or wherever your FastAPI app is
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # or "*" for dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
