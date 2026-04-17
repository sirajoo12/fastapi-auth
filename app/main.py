from fastapi import FastAPI

from auth.router import router as auth_router
from database.base import Base
from database.session import engine

app = FastAPI()

# create tables
Base.metadata.create_all(bind=engine)

# include auth routes
app.include_router(auth_router, prefix="/auth")


@app.get("/")
def home():
    return {"message": "Auth system running 🚀"}
