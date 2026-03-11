import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import Integer, String, Date
from dotenv import load_dotenv
import os

# connection requirements (from CLI)
# username
# password
# database name
# host
# port

# Authentication - ID verification
# Authorizaiton - What are you allowed to do

# Connection string - Driver://username:password@host:port/database
# HARDCODE TO VERIFY IT WORKS, THEN REMOVE DO NOT COMMIT BETWEEN SHOULD NEVER END UP ON GITHUB
# secret file
# .env

# gathering connection string
load_dotenv()
CS = os.getenv("CS")
engine = create_engine(CS)

# prepping the query
query = "SELECT * FROM associates"
df = pd.read_sql(query, engine)
print(df)

df.to_sql(
    name="processed",
    con = engine,
    index = False,
    if_exists = "replace",
    dtype = {
        "associate_id": Integer,
        "first_name": String(50),
        "last_name": String(50),
        "email": String(115),
        "hire_date": Date,
        "department": String(50)
    }
)

print("Wrote to db")

from sqlalchemy.orm import DeclarativeBase, Mapped

class Base(DeclarativeBase):
    pass

class Cohort(Base):
    __tablename__ = "cohorts"
    
    id: Mapped[int]
    start_date: Mapped[Date]
    curriculum: Mapped[str]
    trainees: Mapped[list["Trainee"]]



class Trainee(Base):
    __tablename__ = "trainees"

    id: Mapped[int]
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str]
    hire_date: Mapped[Date]
    department: Mapped[str]
    cohort: Mapped["Cohort"]