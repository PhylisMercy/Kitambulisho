#!/usr/bin/python3
""" State Module for HBNB project """
import os
import enum
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, DateTime, Enum
from sqlalchemy.orm import backref

STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')





class Kitambulisho(BaseModel, Base):
    """Kitambulisho class handles all application vitambulisho
    user_identity_image = Image_url
    user_signature_urls = Signature_url
    """
    if STORAGE_TYPE == "db":
        __tablename__ = 'vitambulisho'
        # backref for kitambulisho to collector register 
        kitambulisho_Collection_Register = relationship("Kitambulisho_Collection_Register", backref="kitambulisho")
        # backref for kitambulisho to collector signoff 
        # kitambulisho_Collection_SignOff = relationship("Kitambulisho_Collection_Station_SignOff", backref="kitambulisho")
        # recovered_on = Column(DateTime, nullable=True)
        cleared_on = Column(DateTime, nullable=True)

        name = Column(String(128), nullable=False)
        surname = Column(String(128), nullable=True)
        ID_Number = Column(String(128), nullable=False)
        ID_found_at_longitude = Column(String(128), nullable=True)
        ID_found_at_latitude = Column(String(128), nullable=True)
        Birth_District = Column(String(128), nullable=True)
        Image_url = Column(String(255), nullable=True)
        Signature_url = Column(String(255), nullable=True)

