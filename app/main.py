import sys
import os

# Add the backend directory to the sys.path
#sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from fastapi import FastAPI
from app.routes import student
from app.routes import technique
from app.routes import classification
from app.routes import rank
from app.routes import session
from app.routes import tag
from config import verify_connection  # Import the function
 
app = FastAPI()

app.include_router(student.router, prefix="/api")
app.include_router(technique.router, prefix="/api")
app.include_router(classification.router, prefix="/api")
app.include_router(rank.router, prefix="/api")
app.include_router(session.router, prefix="/api")
app.include_router(tag.router, prefix="/api")


