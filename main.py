from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import contact
from database import Base, engine
from routers import chatbot

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Prompter Backend", version="1.0")

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
app.include_router(chatbot.router)
app.include_router(contact.router)

@app.get("/")
def root():
    return {"message": "Prompter Backend  🚀"}
