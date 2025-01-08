from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, oath2
from ..database import get_db



router = APIRouter(
    prefix="/stats",
    tags=['Stats']
)

@router.get("/mood-chart")
def get_mood_chart_data(db: Session = Depends(get_db), current_user: int = Depends(oath2.get_current_user)):
    mood_entries = db.query(models.Mood).filter(models.Mood.owner_id == current_user.id).all()

    mood_data = {"rad": 0, "good": 0, "meh": 0, "bad": 0, "awful": 0}

    for entry in mood_entries:
        mood = entry.title
        if mood in mood_data:
            mood_data[mood] += 1

    return mood_data