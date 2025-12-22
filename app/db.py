import sqlalchemy as sa
import os

DATABASE_URL = os.getenv("DATABASE_URL")

engine = sa.create_engine(DATABASE_URL, pool_pre_ping=True)
metadata = sa.MetaData()