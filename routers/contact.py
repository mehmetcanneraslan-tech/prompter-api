from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import ContactMessage
from schemas import ContactMessageCreate, ContactMessageOut
from database import get_db
from utils import send_contact_email, send_confirmation_email  # 📧 ikinci fonksiyon eklendi

router = APIRouter(prefix="/contact", tags=["Contact"])


@router.post("/", response_model=ContactMessageOut)
def send_message(data: ContactMessageCreate, db: Session = Depends(get_db)):
    """
    İletişim formundan gelen mesajı veritabanına kaydeder,
    yöneticiyi e-posta ile bilgilendirir,
    ve kullanıcıya bilgilendirme e-postası gönderir.
    """
    # 💾 Veritabanına kaydet
    new_msg = ContactMessage(**data.dict())
    db.add(new_msg)
    db.commit()
    db.refresh(new_msg)

    # 📧 Admin'e e-posta gönder
    send_contact_email(data.name, data.email, data.phone, data.message)

    # 📩 Kullanıcıya bilgilendirme e-postası gönder
    send_confirmation_email(data.email, data.name)

    return new_msg
