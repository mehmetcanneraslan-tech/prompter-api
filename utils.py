import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT", "465"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
MAIL_RECEIVER = os.getenv("MAIL_RECEIVER")

def send_contact_email(name, email, phone, message):
    subject = "Yeni İletişim Formu Mesajı"
    body = f"""
    Yeni bir iletişim formu gönderildi:

    Ad Soyad: {name}
    E-posta: {email}
    Telefon: {phone or "-"}
    Mesaj:
    {message}
    """

    msg = MIMEMultipart()
    msg["From"] = SMTP_USER
    msg["To"] = MAIL_RECEIVER
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        # 🔽 Sertifika doğrulaması devre dışı (ama bağlantı hâlâ SSL)
        context = ssl._create_unverified_context()
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=context) as server:
            server.login(SMTP_USER, SMTP_PASS)
            server.send_message(msg)
            print("📨 E-posta başarıyla gönderildi (SSL, verify off).")
    except Exception as e:
        print(f"❌ E-posta gönderimi başarısız: {e}")

# ✅ Kullanıcıya bilgilendirme maili gönder
def send_confirmation_email(to_email, name):
    subject = "Mesajınız Başarıyla İletildi"
    body = f"""
    Merhaba {name},

    Mesajınızı aldık. En kısa sürede sizinle iletişime geçeceğiz.
    Gönderiminiz başarıyla alınmıştır.

    Saygılarımızla,
    {os.getenv("COMPANY_NAME", "Kurumsal Destek Ekibi")}
    """

    msg = MIMEMultipart()
    msg["From"] = SMTP_USER
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
  #deneme
    try:
        context = ssl._create_unverified_context()
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=context) as server:
            server.login(SMTP_USER, SMTP_PASS)
            server.send_message(msg)
            print(f"📩 {to_email} adresine bilgilendirme e-postası gönderildi.")
    except Exception as e:
        print(f"❌ Bilgilendirme e-postası gönderilemedi: {e}")