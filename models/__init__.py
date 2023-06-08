#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

from sqlalchemy.exc import OperationalError

from models.base_model import BaseModel
from models.city import City
from models.Collection_Stations import Kitambulisho_Collection_Station
from models.collector_signoff import Kitambulisho_Collection_Station_SignOff
from models.Counties import County
from models.Kitambulisho_Collection_Register import Kitambulisho_Collection_Register
from models.review import Review
from models.user import User
from models.vitambulisho import Kitambulisho

if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
    from models.engine import db_storage
    CNC = db_storage.DBStorage.classes
    storage = db_storage.DBStorage()
    try:
        storage.reload()
    except OperationalError as e:
        # handle Unknown database by creating the database natively in sqlalchemy
        # Utilize the ORM in doing this.
        # provide the least privilege for the current user by prompting root login.
        storage.reload()

else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
