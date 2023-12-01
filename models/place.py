#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey as Fk, Integer, Float, Table
from sqlalchemy.orm import relationship as rel
from os import getenv


place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', String(60), Fk('places.id'), primary_key=True),
    Column('amenity_id', String(60), Fk('amenities.id'), primary_key=True)
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), Fk('cities.id'), nullable=False)
    user_id = Column(String(60), Fk('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = rel('Review', backref='place')
        amenities = rel('Amenity', secondary=place_amenity, viewonly=False)
    else:
        @property
        def reviews(self):
            """returns list of reviews"""
            from models import storage
            from models.review import Review
            list = []
            for rev in storage.all(Review).values():
                if rev.place_id == self.id:
                    list.append(rev)
            return list

        @property
        def amenities(self):
            """returns list of amenities"""
            from models import storage
            from models.amenity import Amenity
            list = []
            for amen in storage.all(Amenity).values():
                if amen.place_id == self.id:
                    list.append(amen)
            return list

        @amenities.setter
        def amenities(self, obj):
            """setter for amenity"""
            from models.amenity import Amenity
            if obj and isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
