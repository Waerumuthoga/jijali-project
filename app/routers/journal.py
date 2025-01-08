from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import models, schemas, oath2
from ..database import get_db

router = APIRouter(
    prefix="/journals",
    tags=['Journals']
)

@router.get("/", response_model=List[schemas.Journal])
def get_journals(db: Session = Depends(get_db), current_user: int = Depends(oath2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):

    print(limit)
    journals = db.query(models.Journal).filter(models.Journal.owner_id == current_user.id).filter(models.Journal.title.contains(search)).limit(limit).offset(skip).all()
    return journals

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Journal, responses={401: {"description": "Not authenticated (authentication required)"}})
def create_journals(journal: schemas.JournalCreate, db: Session = Depends(get_db), current_user: int = Depends(oath2.get_current_user)):

    print(current_user.email)
    new_journal = models.Journal(owner_id=current_user.id, **journal.dict())
    db.add(new_journal)
    db.commit()
    db.refresh(new_journal)
    return new_journal

@router.get("/{id}", response_model=schemas.Journal)
def get_journal(id: int, db: Session = Depends(get_db), current_user: int = Depends(oath2.get_current_user)):

    print(current_user.email)
    journal = db.query(models.Journal).filter(models.Journal.id == id, models.Journal.owner_id == current_user.id
    ).first()
    if not journal:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"journal with id: {id} was not found")
    return journal

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_journals(id: int, db: Session = Depends(get_db), current_user: int = Depends(oath2.get_current_user)):

    print(current_user.email)
    journal_query = db.query(models.Journal).filter(models.Journal.id == id)

    journal = journal_query.first()

    if journal == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"journal with id: {id} does not exist")
    
    if journal.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= f"Not authorized to perform requested action")
    
    journal_query.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=schemas.Journal)
def update_journal(id: int, updated_journal: schemas.JournalCreate, db: Session = Depends(get_db), current_user: int = Depends(oath2.get_current_user)):
    

    print(current_user.email)
    journal_querry = db.query(models.Journal).filter(models.Journal.id == id)

    journal = journal_querry.first()
    
    if journal == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"journal with id: {id} does not exist")
    
    if journal.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= f"Not authorized to perform requested action")
    
    journal_querry.update(updated_journal.dict(), synchronize_session=False)

    db.commit()
    
    return journal_querry.first()