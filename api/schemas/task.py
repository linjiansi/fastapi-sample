from typing import Optional
from pydantic import BaseModel, Field

# Base class
class TaskBase(BaseModel):
  title: Optional[str] = Field(None, title="The title of the task")

# Request body
class TaskCreate(TaskBase):
  pass

# Response body
class Task(TaskBase):
  id: int
  done: bool = Field(False, title="Whether the task is done or not")

  class Config:
    orm_mode = True

class TaskCreateResponse(TaskCreate):
  id: int

  class Config:
    orm_mode = True
