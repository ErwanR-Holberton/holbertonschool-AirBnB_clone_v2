#!/usr/bin/python3
""" amenities Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship as rel
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """amenity table"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = rel('Place', secondary=place_amenity, viewonly=False)
