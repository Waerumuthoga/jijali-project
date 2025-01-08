from pydantic import BaseModel, EmailStr, ConfigDict, validator
from datetime import datetime
from typing import Optional


class JournalBase(BaseModel):
    title: str
    status: bool = False
    todays_happenings: str
    special_moments: str
    redo_your_day: str
    handling_stress: str
    done_different: str
    thoughts_and_emotions: str
    gratitude: str
    goals_and_intentions: str

class JournalCreate(JournalBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    username: str
    created_at: datetime

    class Config:
        #orm_mode = True
        model_config = ConfigDict(from_attributes=True)
        
class Journal(JournalBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        #orm_mode = True
        model_config = ConfigDict(from_attributes=True)
    

class MoodBase(BaseModel):
     title: str
     status: bool = False
     mood: str
     feel: str
     todays_influence: str
     mood_shift: str
     fears_and_anxieties: str
     affect: str
     steps: str
     negative_thoughts: str
     main_thoughts: str
     support: str

class MoodCreate(MoodBase):
    pass


class Mood(MoodBase):
   id: int
   created_at: datetime
   owner_id: int
   owner: UserOut
   
   class Config:
        #orm_mode = True
        model_config = ConfigDict(from_attributes=True)


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str
    confirm_password: str

    @validator('confirm_password')
    def passwords_match(cls, v, values):
        if 'password' in values and values['password'] != v:
            raise ValueError('Passwords do not match')
        return v



class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class PasswordReset(BaseModel):
    pass