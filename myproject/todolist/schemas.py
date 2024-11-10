from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TodoSchema(BaseModel):
    title: str
    description: Optional[str] = None
    created_at: datetime
    completed: bool
