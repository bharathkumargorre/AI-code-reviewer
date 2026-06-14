from fastapi import FastAPI
from app.database import engine
from app import models
from app.routers import users, auth_router, upload, review, dashboard

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="AI Code Reviewer"
)

# Include routers
app.include_router(users.router)
app.include_router(auth_router.router)
app.include_router(upload.router)
app.include_router(review.router)
app.include_router(dashboard.router)


@app.get("/")
def home():
    return {
        "message": "AI Code Reviewer Running Successfully 🚀"
    }