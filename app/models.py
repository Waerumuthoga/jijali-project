from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship

from .database import Base

class Journal(Base):
    __tablename__ = "journals"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=True)
    todays_happenings = Column(String, nullable=False)
    special_moments = Column(String, nullable=False)
    redo_your_day = Column(String, nullable=False)
    handling_stress = Column(String, nullable=False)
    done_different = Column(String, nullable=False)
    thoughts_and_emotions = Column(String, nullable=False)
    gratitude = Column(String, nullable=False)
    goals_and_intentions = Column(String, nullable=False)
    status = Column(Boolean, server_default='False')# false for draft, true for completed
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))



class Mood(Base):
    __tablename__ = "moods"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=True)
    mood = Column(String, nullable=False)
    feel = Column(String, nullable=False)
    todays_influence = Column(String, nullable=False)
    mood_shift = Column(String, nullable=False)
    fears_and_anxieties = Column(String, nullable=False)
    affect = Column(String, nullable=False)
    steps = Column(String, nullable=False)
    negative_thoughts = Column(String, nullable=False)
    main_thoughts = Column(String, nullable=True)
    support = Column(String, nullable=False)
    status = Column(Boolean, server_default='False')# false for draft, true for completed
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")