import sys
import os

# Add the backend directory to the sys.path
#sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from fastapi import FastAPI
from backend.routes import student
from backend.routes import technique
from backend.routes import classification
from backend.routes import rank
from backend.routes import session
from backend.routes import tag
from config import verify_connection  # Import the function
 
app = FastAPI()

app.include_router(student.router, prefix="/api")
app.include_router(technique.router, prefix="/api")
app.include_router(classification.router, prefix="/api")
app.include_router(rank.router, prefix="/api")
app.include_router(session.router, prefix="/api")
app.include_router(tag.router, prefix="/api")


