from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from classes_keeper.database_setup import Base

engine = create_engine('sqlite:///school.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
