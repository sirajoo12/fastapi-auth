from fastapi import FastAPI
from app.auth.router import router as auth_router
from app.database.base import Base
from app.database.session import engine

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI Auth System",
    version="1.0.0",
    description="Production-ready authentication system with JWT"
)

# Register routers
app.include_router(auth_router, prefix="/auth", tags=["Auth"])

@app.get("/")
def home():
    return {"message": "Auth system running 🚀"}
