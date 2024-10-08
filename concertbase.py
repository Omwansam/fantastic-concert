from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///concerts.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session=Session()