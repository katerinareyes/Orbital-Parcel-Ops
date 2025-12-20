import sqlalchemy as sa
import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    pool_pre_ping=True,
    )

engine = sa.create_engine(DATABASE_URL)
metadata = sa.MetaData()