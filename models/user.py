#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship as rel


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = rel('Place', backref='user')
