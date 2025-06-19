from sqlalchemy.orm import Session
import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_skill(db: Session, skill: schemas.SkillBase):
    db_skill = models.Skill(name=skill.name, category=skill.category)
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill

def add_user_skill_have(db: Session, data: schemas.SkillAssociation):
    entry = models.UserSkillHave(user_id=data.user_id, skill_id=data.skill_id)
    db.add(entry)
    db.commit()
    return {"status": "added to skills_have"}

def add_user_skill_want(db: Session, data: schemas.SkillAssociation):
    entry = models.UserSkillWant(user_id=data.user_id, skill_id=data.skill_id)
    db.add(entry)
    db.commit()
    return {"status": "added to skills_want"}

def get_users(db: Session):
    return db.query(models.User).all()
