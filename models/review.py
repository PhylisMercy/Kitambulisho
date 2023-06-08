#!/usr/bin/python3
""" Review module for the HBNB project """
import os

from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')


class Review(BaseModel, Base):
    """Review class handles all application reviews"""
    if STORAGE_TYPE == "db":
        __tablename__ = 'reviews'
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        # backref to Collection Register
        review_user = relationship('User', backref="user_reviewer")
        station_id = Column(String(60), ForeignKey('Kitambulisho_Collection_Stations.id'), nullable=False)
        Collection_Station = relationship('Kitambulisho_Collection_Station', backref="station_review")
        description = Column(String(1024), nullable=False)

    else:
        place_id = ''
        user_id = ''
        text = ''
