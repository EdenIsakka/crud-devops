
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://neondb_owner:npg_8HJQDEgrF9pT@ep-weathered-sound-acwm58gr-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
