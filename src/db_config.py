from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import logging

# Load environment variables from .env file
load_dotenv()

# Fetch the database URL from the .env file
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the .env file.")

engine = create_engine(DATABASE_URL, echo=True)

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

logging.getLogger('sqlalchemy.engine.Engine').setLevel(logging.WARNING)
