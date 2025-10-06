from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import ContactMessage
from schemas import ContactMessageCreate, ContactMessageOut
from database import get_db
from utils import send_contact_email  # 📧 yeni ekledik

router = APIRouter(prefix="/contact", tags=["Contact"])

@router.post("/", response_model=ContactMessageOut)
def send_message(data: ContactMessageCreate, db: Session = Depends(get_db)):
    """
    İletişim formundan gelen mesajı veritabanına kaydeder
    ve yöneticiyi e-posta ile bilgilendirir.
    """
    new_msg = ContactMessage(**data.dict())
    db.add(new_msg)
    db.commit()
    db.refresh(new_msg)

    # 📧 E-posta gönderimi
    send_contact_email(data.name, data.email, data.phone, data.message)

    return new_msg
