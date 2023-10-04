# models/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databases import Database
from models.database import Base
import os
from dotenv import load_dotenv

load_dotenv()



DATABASE_URL = os.getenv("DATABASE_URL")

# Create a Database instance
database = Database(DATABASE_URL)

# SQLAlchemy models and SessionLocal
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)
