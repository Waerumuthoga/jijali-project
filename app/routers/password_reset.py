from fastapi import APIRouter, BackgroundTasks, status, HTTPException, Depends, APIRouter, Request
from pydantic import EmailStr
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from fastapi.templating import Jinja2Templates
from .. import database, schemas, models, utils, oath2
from fastapi.responses import HTMLResponse

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.get("/password_reset", response_class=HTMLResponse)
async def get_password_reset_page(request: Request):
    return templates.TemplateResponse("password_reset.html", {"request": request})

@router.post("/forgot-password", status_code=status.HTTP_200_OK, response_model=schemas.PasswordReset)
def forgot_password(email: EmailStr, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    token = utils.create_password_reset_token(email=email)
    
    reset_link = f"http://example.com/reset-password?token={token}"

    return JSONResponse(content={"message": "Password reset link sent"}, status_code=status.HTTP_200_OK)

@router.post("/reset-password", status_code=status.HTTP_200_OK, response_model=schemas.PasswordReset)
def reset_password(token: str, new_password: str, db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token", headers={"WWW-Authenticate": "Bearer"})

    email = utils.verify_password_reset_token(token, credentials_exception)
    
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    

    hashed_password = utils.get_password_hash(new_password)
    user.password = hashed_password
    db.commit()
    
    return JSONResponse(content={"message": "Password successfully updated"}, status_code=status.HTTP_200_OK)