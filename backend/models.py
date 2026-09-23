from sqlalchemy import Column, Integer, String, Text
from backend.database import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    required_skills = Column(Text, nullable=False)
    minimum_experience = Column(Integer, nullable=False)