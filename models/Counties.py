#!/usr/bin/python3
""" County Module for HBNB project """
import os

from sqlalchemy.orm import relationship

import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')


class County(BaseModel, Base):
    """ County class """
    if STORAGE_TYPE == "db":
        __tablename__ = 'Counties'
        name = Column(String(128), nullable=False, unique=True)
        cities = relationship('City', backref='county_cities', cascade='all, delete, delete-orphan')
    else:
        name = ''

        @property
        def cities(self):
            """
                getter method, returns list of City objs from storage
                linked to the current County
            """
            city_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
