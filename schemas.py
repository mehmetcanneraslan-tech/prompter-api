from pydantic import BaseModel, EmailStr, constr
from datetime import datetime

class ContactMessageCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str | None = None
    message: str

class ContactMessageOut(ContactMessageCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
