from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import contact
from database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Prompter Backend", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(contact.router)

@app.get("/")
def root():
    return {"message": "Prompter Backend  🚀"}
