from sqlalchemy import create_engine, MetaData
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)
metadata = MetaData()
