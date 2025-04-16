from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...database import get_db
from ...models import Review as ReviewModel
from ...schemas.review import ReviewCreate, Review
from sqlalchemy.orm import joinedload

router = APIRouter()

@router.post("/reviews/", response_model=Review)
def criar_review(review: ReviewCreate, db: Session = Depends(get_db)):
    db_review = ReviewModel(**review.model_dump())
    db.add(db_review)
    db.commit()

    # Recarrega com os relacionamentos
    db_review = db.query(ReviewModel)\
        .options(joinedload(ReviewModel.usuario), joinedload(ReviewModel.filme))\
        .filter_by(id_usuario=review.id_usuario, id_filme=review.id_filme)\
        .first()

    return db_review


@router.get("/reviews/", response_model=list[Review])
def listar_reviews(db: Session = Depends(get_db)):
    return db.query(ReviewModel)\
             .options(joinedload(ReviewModel.usuario), joinedload(ReviewModel.filme))\
             .all()