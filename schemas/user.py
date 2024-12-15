from pydantic import BaseModel

# User registration schema
class UserCreate(BaseModel):
    username: str
    password: str
    role: str

# User login schema
class UserLogin(BaseModel):
    username: str
    password: str
