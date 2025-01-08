from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter, Request, Form
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

templates = Jinja2Templates(directory="app/templates")

@router.get("/register", response_class=HTMLResponse)
async def get_register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})



@router.post("/register", status_code=status.HTTP_201_CREATED)
def create_user(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    confirm_password: str = Form(...),
    db: Session = Depends(get_db)
):
    if password != confirm_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Passwords do not match")

    hashed_password = utils.hash(password)

    new_user = models.User(
        username=username,
        email=email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"message": "User created successfully"}


@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
   
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User with id: {id} does not exist")
    return user