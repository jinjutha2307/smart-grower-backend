from fastapi import FastAPI
from app.database import engine
from app import models, schemas
from fastapi.middleware.cors import CORSMiddleware
from app.routers import locations, growers
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust as needed for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(locations.router)
app.include_router(growers.router)
