from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import crud, schemas

# Create all tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Skill Sharing Platform is online!"}

@app.post("/users/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)
@app.post("/skills/")
def create_skill(skill: schemas.SkillBase, db: Session = Depends(get_db)):
    return crud.create_skill(db=db, skill=skill)
@app.post("/skills/have/")
def add_skill_have(skill_data: schemas.SkillAssociation, db: Session = Depends(get_db)):
    return crud.add_user_skill_have(db=db, data=skill_data)
    
@app.post("/skills/want/")
def add_skill_want(skill_data: schemas.SkillAssociation, db: Session = Depends(get_db)):
    return crud.add_user_skill_want(db=db, data=skill_data)

@app.get("/skills/")
def get_skills(db: Session = Depends(get_db)):
    return db.query(models.Skill).all()

@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)
    
@app.get("/skills/have/")
def get_skills_have(db: Session = Depends(get_db)):
    return db.query(models.UserSkillHave).all()
    
@app.get("/skills/want/")
def get_skills_want(db: Session = Depends(get_db)):
    return db.query(models.UserSkillWant).all()
    
@app.get("/skills/have/{user_id}")
def get_user_skills_have(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.UserSkillHave).filter(models.UserSkillHave.user_id == user_id).all()

@app.get("/skills/want/{user_id}")
def get_user_skills_want(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.UserSkillWant).filter(models.UserSkillWant.user_id == user_id).all()
    
@app.get("/skills/have/{user_id}")
def get_user_skills_have(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.UserSkillHave).filter(models.UserSkillHave.user_id == user_id).all()

@app.get("/skills/want/{user_id}")
def get_user_skills_want(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.UserSkillWant).filter(models.UserSkillWant.user_id == user_id).all()
