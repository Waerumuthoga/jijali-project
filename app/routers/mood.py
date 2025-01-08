from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import models, schemas, oath2
from ..database import get_db

router = APIRouter(
    prefix="/moods",
    tags=['Moods']
)

@router.get("/", response_model=List[schemas.Mood])
def get_moods(db: Session = Depends(get_db), current_user: int = Depends(oath2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):

    print(limit)
    moods = db.query(models.Mood).filter(models.Mood.owner_id == current_user.id).filter(models.Mood.title.contains(search)).limit(limit).offset(skip).all()
    return moods

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Mood)
def create_moods(mood: schemas.MoodCreate, db: Session = Depends(get_db), current_user: int = Depends(oath2.get_current_user)):

    print(current_user.email)
    new_mood = models.Mood(owner_id=current_user.id,**mood.dict())
    db.add(new_mood)
    db.commit()
    db.refresh(new_mood)
    return new_mood

@router.get("/{id}", response_model=schemas.Mood)
def get_mood(id: int, db: Session = Depends(get_db), current_user: int = Depends(oath2.get_current_user)):
    
    print(current_user.email)
    mood = db.query(models.Mood).filter(models.Mood.id == id, models.Mood.owner_id == current_user.id
    ).first()
    if not mood:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"mood with id: {id} was not found")
    return mood

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_moods(id: int, db: Session = Depends(get_db), current_user: int = Depends(oath2.get_current_user)):
    
    print(current_user.email)
    mood_query = db.query(models.Mood).filter(models.Mood.id == id)

    mood = mood_query.first()

    if mood == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"mood with id: {id} does not exist")
    
    if mood.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= f"Not authorized to perform requested action")
    
    mood_query.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=schemas.Mood)
def update_mood(id: int, updated_mood: schemas.MoodCreate, db: Session = Depends(get_db), current_user: int = Depends(oath2.get_current_user)):
    
    print(current_user.email)
    mood_querry = db.query(models.Mood).filter(models.Mood.id == id)

    mood = mood_querry.first()
    
    if mood == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"mood with id: {id} does not exist")
    
    if mood.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= f"Not authorized to perform requested action")
    
    mood_querry.update(updated_mood.dict(), synchronize_session=False)

    db.commit()
    
    return mood_querry.first()