import pandas as pd
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.types import Integer, String, Date
from dotenv import load_dotenv
from datetime import datetime
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

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Cohort(Base):
    __tablename__ = "cohorts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    start_date: Mapped[datetime] = mapped_column(default=datetime.today())
    curriculum: Mapped[str] = mapped_column(nullable=False)
    trainees: Mapped[list["Trainee"]] = relationship(back_populates="cohort")



class Trainee(Base):
    __tablename__ = "trainees"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    hire_date: Mapped[datetime] = mapped_column(default=datetime.today())
    department: Mapped[str] = mapped_column(nullable=False)

    cohort_id: Mapped[int] = mapped_column(ForeignKey("cohorts.id"))
    cohort: Mapped["Cohort"] = relationship(back_populates="trainees")


Base.metadata.create_all(engine)