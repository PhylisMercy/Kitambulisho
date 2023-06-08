#!/usr/bin/python3
""" City Module for HBNB project """
import os

from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if STORAGE_TYPE == "db":
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False, unique=True)
        # Relationships in sqlalchemy must be defined twice.
        county_id = Column(String(60), ForeignKey('Counties.id'), nullable=False)
        city_county = relationship("County", backref="city_county")
        # relationship btwn county & its collection stations
        # Deletes All orphan places when the parent City is Deleted
        Kitambulisho_Collection_Stations = relationship('Kitambulisho_Collection_Station', backref='cities',
                                                        cascade='all, delete, delete-orphan')

        """ Output a nice looking representation when the class is 
        printed using the __repr__
        """

        def __repr__(self):
            return "<name(%r)>" % self.name

    else:
        state_id = ''
        name = ''
        places = []
