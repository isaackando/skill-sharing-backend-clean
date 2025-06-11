from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

class SkillBase(BaseModel):
    name: str
    category: str

class SkillAssociation(BaseModel):
    user_id: int
    skill_id: int