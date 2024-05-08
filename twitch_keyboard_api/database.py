from sqlalchemy import Boolean, create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///database/main.db", echo=False)

Base = declarative_base()


class Configuration(Base):
    __tablename__ = "configuration"

    id = Column(Integer, primary_key=True)
    channel = Column(String, nullable=False)
    bot_username = Column(String, nullable=True)
    bot_oauth = Column(String, nullable=True)
    last_used = Column(Boolean, nullable=True)


# Initialize the database
Base.metadata.create_all(engine)


# Create a session
SessionMaker = sessionmaker(bind=engine)
session = SessionMaker()
