from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database.base import Base
from datetime import datetime

class Reminder(Base):
    __tablename__ = 'reminders'
    
    id = Column(Integer, primary_key=True)
    reminder_time = Column(DateTime, nullable=False)
    message = Column(String(500))
    is_sent = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Foreign keys
    task_id = Column(Integer, ForeignKey('tasks.id'))
    
    # Relationships
    task = relationship("Task", back_populates="reminders")