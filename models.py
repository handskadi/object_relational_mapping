#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker , relationship

# Declare a Mapping¶
Base = declarative_base()

# User Class

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    email = Column(String(255))

    # Define the one-to-many relationship
    posts = relationship('Post', back_populates='author')

# Post Class
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    content = Column(String(255))
    user_id = Column(Integer, ForeignKey('users.id'))

    # Define the relationship
    author = relationship('User', back_populates='posts')
