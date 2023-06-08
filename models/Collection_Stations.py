#!/usr/bin/python3
""" Kitambulisho_Collection_Station Module for HBNB project """
import os

from models import Kitambulisho_Collection_Register
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey, \
    MetaData, Table, ForeignKey, DateTime
from sqlalchemy.orm import backref

STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')


class Kitambulisho_Collection_Station(BaseModel, Base):
    """Kitambulisho_Collection_Station class handles all application places"""
    if STORAGE_TYPE == "db":
        __tablename__ = 'Kitambulisho_Collection_Stations'
        # backref for remuneration- 
        operate_registration_date = Column(DateTime, nullable=True)
        next_license_renew_date = Column(DateTime, nullable=True)
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        kitambulisho_city = relationship("City", backref="kitambulisho_Stations")

        staff_user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        staff_user = relationship("User", backref="user")

        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

        station_reviews = relationship('Review', backref='kitambulisho_collection_station', cascade='all, delete, delete-orphan')
        # the below connects many to many and grabs the other item in reference table
        # facilitates capturing of all amenities of a place
        amenities = relationship('Kitambulisho', secondary="Kitambulisho_Collection_Register", viewonly=False)
        # query all the collected ID cards
        # facilitates capturing of all collected id cards of a place
        id_collector_signoffs = relationship('Kitambulisho_Collection_Station_SignOff', secondary="Kitambulisho_Collection_Register", viewonly=False)
    else:
        city_id = ''
        user_id = ''
        name = ''
        description = ''
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
        review_ids = []

        @property
        def amenities(self):
            """
                getter for amenitiess list, i.e. amenities attribute of self
            """
            if len(self.amenity_ids) > 0:
                return self.amenity_ids
            else:
                return None

        @amenities.setter
        def amenities(self, amenity_obj):
            """
                setter for amenity_ids
            """
            if amenity_obj and amenity_obj not in self.amenity_ids:
                self.amenity_ids.append(amenity_obj.id)

        @property
        def reviews(self):
            """
                getter for reviews list, i.e. reviews attribute of self
            """
            if len(self.review_ids) > 0:
                return self.review_ids
            else:
                return None

        @reviews.setter
        def reviews(self, review_obj):
            """
                setter for review_ids
            """
            if review_obj and review_obj not in self.review_ids:
                self.review_ids.append(review_obj.id)
