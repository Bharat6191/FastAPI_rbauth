import os
import jwt
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from .models.project import  Project
from .models.user import User
from passlib.context import CryptContext
from schemas import UserCreate, UserLogin, ProjectCreate
from utils.auth import verify_token, authenticate_user, create_access_token
from utils.database import db
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# JWT secret and algorithm
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Route for user registration
@app.post("/register")
async def register_user(user: UserCreate):
    new_user = User(username=user.username, role=user.role)
    new_user.hash_password(user.password)
    new_user.save()
    return {"message": "User registered successfully"}

# Route for user login
@app.post("/login")
async def login_user(user: UserLogin):
    db_user = User.objects(username=user.username).first()
    if db_user and db_user.verify_password(user.password):
        # Generate JWT token
        token = create_access_token(str(db_user.id), db_user.role)
        return {"access_token": token}
    else:
        raise HTTPException(status_code=400, detail="Invalid credentials")

# Route to get projects (accessible to all users)
@app.get("/projects")
async def get_projects(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    projects = Project.objects()
    return projects

# Route to create a project (admin only)
@app.post("/projects")
async def create_project(project: ProjectCreate, token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if not payload or payload["role"] != "admin":
        raise HTTPException(status_code=403, detail="Access denied")
    new_project = Project(name=project.name, description=project.description)
    new_project.save()
    return {"message": "Project created successfully"}
