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
        # Enables for reverse lookup of kitambulisho to the holding/reporting station.
        collection_stations = relationship('Kitambulisho_Collection_Station', secondary="Kitambulisho_Collection_Register", viewonly=False)
        # Enables for reverse lookup of kitambulisho to the Signoff/collected register.
        collection_registers = relationship('Kitambulisho_Collection_Station_SignOff', secondary="Kitambulisho_Collection_Register", viewonly=False)

        name = Column(String(128), nullable=False)
        surname = Column(String(128), nullable=True)
        ID_Number = Column(String(128), nullable=False)
        ID_found_at_longitude = Column(String(128), nullable=True)
        ID_found_at_latitude = Column(String(128), nullable=True)
        Birth_District = Column(String(128), nullable=True)
        Birth_Division= Column(String(128), nullable=True)
        Birth_Location = Column(String(128), nullable=True)
        Birth_Sub_Location = Column(String(128), nullable=True)
        Image_url = Column(String(255), nullable=True)
        Signature_url = Column(String(255), nullable=True)

