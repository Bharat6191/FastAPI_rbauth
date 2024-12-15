import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Generate a random secret key if not already provided in the .env file
secret_key = os.urandom(32).hex()
SECRET_KEY = os.getenv("SECRET_KEY", secret_key)  # Fallback to generated key if not present in environment
ALGORITHM = "HS256"  # Algorithm for JWT
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb+srv://admin:admin@cluster1.wiicw.mongodb.net/rbauth")  # Default MongoDB URI if not specified
