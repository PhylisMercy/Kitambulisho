#!/usr/bin/python3
"""This module defines a class Remuneration"""
import os
import enum
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, DateTime, Numeric, Enum, ForeignKey

STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')
class Kitambulisho_Status(enum.Enum):
    closed = 0
    verification = 1
    anomaly = 2
    pending = 3

class TaxFiledStatus(enum.Enum):
    completed = 0
    processed = 1
    pending = 2


class Kitambulisho_Collection_Station_SignOff(BaseModel, Base):
    """
        ID_Collector_SignOff class handles all application id collector users
    """
    if STORAGE_TYPE == "db":
        __tablename__ = 'ID_Collector_SignOff'
        # backref to remuneration
        # signoff_remunerations = relationship("Remuneration", backref="ID_Collector_SignOff")
        ID_Collector_Register_id = Column(String(60), ForeignKey('Kitambulisho_Collection_Register.id'), nullable=False)
        kitambulisho_register_collect = relationship("Kitambulisho_Collection_Register", backref="station_signoff_id")
        status = Column(Enum(Kitambulisho_Status), default=Kitambulisho_Status.pending)

        # kitambulisho_id = Column(String(60), ForeignKey('vitambulisho.id'), nullable=False)
        # # Delete all enumerations when the station is deleted.
        # kitambulisho = relationship("Kitambulisho", backref="kitambulisho_Collection_Station_SignOffs")
        payment_Transaction_code = Column(String(60), nullable=True)
        Pay_amount = Column(Numeric(10, 2), nullable=True)
        Tax_Charge = Column(Numeric(10, 2), nullable=True)
        Tax_Filed = Column(Enum(TaxFiledStatus), default=TaxFiledStatus.pending)

    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
