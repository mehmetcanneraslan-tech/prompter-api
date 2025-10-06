from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import contact
from database import Base, engine

# Tabloları oluştur
Base.metadata.create_all(bind=engine)

# Uygulama
app = FastAPI(title="Prompter Backend", version="1.0")

# CORS ayarları
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Bolt.new veya Vite
        "http://localhost:3000",  # React
        "https://yourfrontend.vercel.app",  # deploy edince
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Router ekle
app.include_router(contact.router)

@app.get("/")
def root():
    return {"message": "Prompter Backend  🚀"}
