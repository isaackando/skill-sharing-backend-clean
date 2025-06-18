from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, get_db

# Create all database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# ====================
# Middleware
# ====================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ====================
# Root
# ====================
@app.get("/")
def home():
    return {"message": "Skill Sharing Platform is online!"}

# ====================
# User Endpoints
# ====================
@app.post("/users/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

# ====================
# Skill Endpoints
# ====================
@app.post("/skills/")
def create_skill(skill: schemas.SkillBase, db: Session = Depends(get_db)):
    return crud.create_skill(db=db, skill=skill)

@app.get("/skills/")
def get_skills(db: Session = Depends(get_db)):
    return db.query(models.Skill).all()

# ================================
# User-Skill Relationship Endpoints
# ================================
@app.post("/skills/have/")
def add_skill_have(skill_data: schemas.SkillAssociation, db: Session = Depends(get_db)):
    return crud.add_user_skill_have(db=db, data=skill_data)

@app.post("/skills/want/")
def add_skill_want(skill_data: schemas.SkillAssociation, db: Session = Depends(get_db)):
    return crud.add_user_skill_want(db=db, data=skill_data)

@app.get("/skills/have/")
def get_all_user_skills_have(db: Session = Depends(get_db)):
    return db.query(models.UserSkillHave).all()

@app.get("/skills/want/")
def get_all_user_skills_want(db: Session = Depends(get_db)):
    return db.query(models.UserSkillWant).all()

@app.get("/skills/have/{user_id}")
def get_user_skills_have(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.UserSkillHave).filter(models.UserSkillHave.user_id == user_id).all()

@app.get("/skills/want/{user_id}")
def get_user_skills_want(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.UserSkillWant).filter(models.UserSkillWant.user_id == user_id).all()

# ====================
# Health Check
# ====================
@app.get("/health")
def health_check():
    return {"status": "OK"}


