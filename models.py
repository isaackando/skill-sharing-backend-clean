from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    skills_have = relationship("UserSkillHave", backref="user")
    skills_want = relationship("UserSkillWant", backref="user")


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String)
    users_have = relationship("UserSkillHave", backref="skill")
    users_want = relationship("UserSkillWant", backref="skill")


class UserSkillHave(Base):
    __tablename__ = "user_skills_have"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    skill_id = Column(Integer, ForeignKey("skills.id"))


class UserSkillWant(Base):
    __tablename__ = "user_skills_want"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    skill_id = Column(Integer, ForeignKey("skills.id"))