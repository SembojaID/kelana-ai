import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Memuat variabel dari .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Membuat engine koneksi ke PostgreSQL
engine = create_engine(DATABASE_URL)

# Membuat factory session untuk API
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class untuk ORM Model
Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)