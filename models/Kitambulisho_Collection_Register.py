#!/usr/bin/python3
""" Kitambulisho_Collection_Register Module for HBNB project """
import os
import uuid

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey,\
    MetaData, Table, ForeignKey
from sqlalchemy.orm import backref
STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')

if STORAGE_TYPE == "db":
    class Kitambulisho_Collection_Register(BaseModel, Base):
        """ Kitambulisho_Collection_StationAmenity Class """
        __tablename__ = 'Kitambulisho_Collection_Register'
        metadata = Base.metadata
        collection_station_id = Column(String(60),
                          ForeignKey('Kitambulisho_Collection_Stations.id'),
                          nullable=False,
                          primary_key=True)
        # backref to Collection Station
        kitambulisho_Collection_Stations = relationship('Kitambulisho_Collection_Station', backref='kitambulisho_Collection_Register')

        

        kitambulisho_id = Column(String(60),
                            ForeignKey('vitambulisho.id'),
                            nullable=False,
                            primary_key=True)
        # backref to vitambulisho
        kitambulisho_turned_in_station = relationship('Kitambulisho', backref='registered_station_Nid')

        # vitambulisho = relationship('Kitambulisho', backref='kitambulisho_Collection_Register')
        # reviews_id = Column(String(60),
        #                     ForeignKey('reviews.id'),
        #                     nullable=False,
        #                     primary_key=True)
        # ID_Collector_Signoff_id = Column(String(60),
                            # ForeignKey('ID_Collector_SignOff.id'),
                            # nullable=False, index=True,
                            # primary_key=True, default=uuid.uuid4)
        #backref to collector signoff
        register_form_signoffs = relationship("Kitambulisho_Collection_Station_SignOff", backref="register_station")

        # backref to reviews
        # reviews = relationship('Review', backref='kitambulisho_Collection_Register')
