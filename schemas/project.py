from pydantic import BaseModel

# Project creation schema
class ProjectCreate(BaseModel):
    name: str
    description: str
