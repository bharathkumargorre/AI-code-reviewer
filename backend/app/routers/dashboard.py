from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db
from app.models import Review

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/")
def dashboard(db: Session = Depends(get_db)):

    total_reviews = db.query(Review).count()

    average_score = db.query(
        func.avg(Review.score)
    ).scalar()

    highest_score = db.query(
        func.max(Review.score)
    ).scalar()

    lowest_score = db.query(
        func.min(Review.score)
    ).scalar()

    return {
        "total_reviews": total_reviews,
        "average_score": round(average_score, 2) if average_score else 0,
        "highest_score": highest_score,
        "lowest_score": lowest_score
    }