# from fastapi import FastAPI
# from mongoengine import Document, StringField, ReferenceField
# # from .user import User

# # class Project(Document):
# #     name = StringField(required=True, max_length=100)
# #     description = StringField(max_length=255)
# #     created_by = ReferenceField(User, required=True)

# from mongoengine import connect

# from config import MONGODB_URI
# connect(db="rbauth", host=MONGODB_URI)

# class Project(Document):
#     name = StringField(required=True)
#     description = StringField()

# app = FastAPI()

# # Function to create a project
# @app.post("/projects")
# def create_project(name: str, description: str):
#     project = Project(name=name, description=description)
#     project.save()  # This saves the project to the database
#     return {"id": str(project.id), "name": project.name, "description": project.description}


# # Function to get all projects (Read)
# @app.get("/projects")
# def get_all_projects():
#     return Project.objects.all()

# # Function to update a project
# @app.put("/projects/{project_id}")
# def update_project(project_id: str, name: str = None, description: str = None):
#     project = Project.objects.get(id=project_id)
#     if name:
#         project.name = name
#     if description:
#         project.description = description
#     project.save()
#     return {"id": str(project.id), "name": project.name, "description": project.description}


# # Function to delete a project
# @app.delete("/projects/{project_id}")
# def delete_project(project_id: str):
#     project = Project.objects.get(id=project_id)
#     project.delete()
#     return {"status": "deleted"}
from mongoengine import Document, StringField

class Project(Document):
    name = StringField(required=True)
    description = StringField(required=True)
