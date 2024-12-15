# # from mongoengine import Document, StringField, IntField
# # from passlib.context import CryptContext
# # # from ..utils.database import db

# # pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# # class User(Document):
# #     username = StringField(required=True, unique=True, max_length=50)
# #     password = StringField(required=True, max_length=128)
# #     role = StringField(default="user")

# #     def set_password(self, password: str):
# #         self.password = pwd_context.hash(password)

# #     def check_password(self, password: str):
# #         return pwd_context.verify(password, self.password) # type: ignore
# from config import MONGODB_URI
# from mongoengine import connect
# connect(db="rbauth", host=MONGODB_URI)

# class User(Document):
#     username = StringField(required=True, unique=True)
#     password = StringField(required=True)  # Example fields for demonstration

# # Example function for user registration
# def register_user(username, password):
#     user = User(username=username, password=password)  # Hash password as needed
#     user.save()  # Save user to the database

# # Example function for user login
# def login_user(username, password):
#     user = User.objects(username=username).first()  # Find user by username
#     if user and user.password == password:  # Compare passwords (hash as needed)
#         # Generate JWT token
#         return {"access_token": "JWT_TOKEN"}
#     return None



# from mongoengine import Document, StringField
# from passlib.hash import bcrypt

# class User(Document):
#     username = StringField(required=True, unique=True)
#     password = StringField(required=True)
#     role = StringField(default="user")

#     def hash_password(self, password):
#         self.password = bcrypt.hash(password)

#     def verify_password(self, password):
#         return bcrypt.verify(password, self.password)

from mongoengine import Document, StringField
from passlib.hash import bcrypt

class User(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)
    role = StringField(default="user")

    def hash_password(self, password):
        self.password = bcrypt.hash(password)

    def verify_password(self, password):
        return bcrypt.verify(password, self.password)
