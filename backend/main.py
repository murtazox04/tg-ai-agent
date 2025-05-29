from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import router as api_router

app = FastAPI(
    title="AI Assistant Backend",
    description="FastAPI backend for Telegram AI Assistant",
    version="1.0.0",
)

# CORS (if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set this properly for production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router, prefix="/api")


# Simple healthcheck
@app.get("/")
async def root():
    return {"status": "ok", "message": "AI Backend is running"}
