from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.review_engine import review_code
from app.database import get_db
from app.models import Review
from app.pdf_report import generate_pdf

router = APIRouter(
    prefix="/review",
    tags=["AI Review"]
)


@router.post("/")
def review(data: dict):

    code = data["code"]

    result = review_code(code)

    return {
        "analysis": result
    }


@router.get("/file/{filename}")
def review_file(
    filename: str,
    db: Session = Depends(get_db)
):

    filepath = f"app/uploads/{filename}"

    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()

    result = review_code(code)

    pdf_file = generate_pdf(
    filename,
    result
)
    new_review = Review(
        filename=filename,
        score=result["quality_score"],
        review=str(result)
    )

    db.add(new_review)
    db.commit()
    db.refresh(new_review)

    return {
        "filename": filename,
        "analysis": result,
        "pdf_report": pdf_file
    }


@router.get("/history")
def review_history(
    db: Session = Depends(get_db)
):

    reviews = db.query(Review).all()

    return reviews