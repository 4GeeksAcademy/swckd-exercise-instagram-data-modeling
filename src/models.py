import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    content = Column(String(500), nullable=False)
    created_at = Column(String(500), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))

class Following(Base):
    __tablename__ = 'following'
    id = Column(Integer, primary_key=True)
    follower_id = Column(Integer, ForeignKey('user.id'))
    followed_id = Column(Integer, ForeignKey('user.id'))

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    followed_id = Column(Integer, ForeignKey('user.id'))
    followed_by_id = Column(Integer, ForeignKey('user.id'))
