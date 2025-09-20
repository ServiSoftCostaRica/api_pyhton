from typing import Optional
from pydantic import BaseModel

class GenericResponse(BaseModel):
    input: Optional[object]
    status: int
    message: str
    results: Optional[object]

    class Config:
        orm_mode = True