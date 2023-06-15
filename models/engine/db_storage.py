#!/usr/bin/python3
"""
Database engine
"""

import os
from sqlalchemy import create_engine, MetaData, select
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.city import City
from models.Collection_Stations import Kitambulisho_Collection_Station
from models.collector_signoff import Kitambulisho_Collection_Station_SignOff
from models.Counties import County
from models.Kitambulisho_Collection_Register import Kitambulisho_Collection_Register
from models.review import Review
from models.user import User
from models.vitambulisho import Kitambulisho
import datetime


class DBStorage:
    """
        handles long term storage of all class instances
    """
    classes = {
        'City': City,
        'Kitambulisho_Collection_Station': Kitambulisho_Collection_Station,
        'Kitambulisho_Collection_Station_SignOff': Kitambulisho_Collection_Station_SignOff,
        'County': County,
        'Kitambulisho_Collection_Register': Kitambulisho_Collection_Register,
        'Review': Review,
        'User': User,
        'Kitambulisho': Kitambulisho,
    }

    """
        handles storage for database
    """
    __engine = None
    __session = None

    def __init__(self):
        """
            creates the engine self.__engine
        """
        self.__class__.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                os.environ.get('HBNB_MYSQL_USER'),
                os.environ.get('HBNB_MYSQL_PWD'),
                os.environ.get('HBNB_MYSQL_HOST'),
                os.environ.get('HBNB_MYSQL_DB')), pool_pre_ping=True)

        if os.environ.get("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__class__.__engine)

    def all(self, cls=None):
        """
           returns a dictionary of all objects
        """
        obj_dict = {}
        if cls is not None:
            try:
                a_query = self.__class__.__session.query(DBStorage.classes[cls])
            except:
                return {}
            for obj in a_query:
                obj_ref = "{}.{}".format(type(obj).__name__, obj.id)
                obj_dict[obj_ref] = obj
            return obj_dict

        for c in DBStorage.classes.values():
            a_query = self.__class__.__session.query(c)
            for obj in a_query:
                obj_ref = "{}.{}".format(type(obj).__name__, obj.id)
                obj_dict[obj_ref] = obj
        return obj_dict

    def new(self, obj):
        """
            adds objects to current database session
        """
        self.__class__.__session.add(obj)

    def save(self):
        """
            commits all changes of current database session
        """
        self.__class__.__session.commit()

    def rollback_session(self):
        """
            rollsback a session in the event of an exception
        """
        self.__class__.__session.rollback()

    def delete(self, obj=None):
        """
            deletes obj from current database session if not None
        """
        if obj:
            self.__class__.__session.delete(obj)
            self.save()
            return True
        return False

    def reload(self):
        """
           creates all tables in database & session from engine
        """
        Base.metadata.create_all(self.__engine)
        self.__class__.__session = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False))

    def close(self):
        """
            calls remove() on private session attribute (self.session)
        """
        self.__class__.__session.close()

    def get(self, cls=None, id=None):
        """
            retrieves one object based on class name and id
        """
        if cls and id:
            fetch = "{}.{}".format(cls, id)
            all_obj = self.all(cls)
            return all_obj.get(fetch)
        return None

    def count(self, cls=None):
        """
            returns the count of all objects in storage
        """
        if cls:
            return len(self.all(cls))
        else:
            return len(self.all())

    def attributes(self):
        """Returns the valid attributes and their types for classname."""
        attributes = {
            "BaseModel":
                {"id": str,
                 "created_at": datetime.datetime,
                 "updated_at": datetime.datetime},
            "City":
                {"county_id": str,
                 "name": str},
            "Kitambulisho_Collection_Station":
                {
                    "operate_registration_date": datetime.datetime,
                    "next_license_renew_date": datetime.datetime,
                    "city_id": str,
                    "staff_user_id": str,
                    "name": str,
                    "latitude": float,
                    "longitude": float,
                },
            "Kitambulisho_Collection_Station_SignOff":
                {
                    "kitambulisho_id": str,
                    "payment_Transaction_code": str,
                    "Pay_amount": float,
                    "Tax_Charge": float,
                    "Tax_Filed": int
                },
            "State":
                {"name": str},
            "Kitambulisho_Collection_Register":
                {
                    "collection_station_id": str,
                    "kitambulisho_id": str,
                    "reviews_id": str,
                },
            "Review":
                {
                    "user_id": str,
                    "document_condition": str,
                    "ID_found_at_longitude": float,
                    "ID_found_at_latitude": float,
                },
            "User":
                {"email": str,
                 "password": str,
                 "first_name": str,
                 "last_name": str
                 },
            "Kitambulisho":
                {
                    "reported_lost_on": datetime.datetime,
                    "cleared_on": datetime.datetime,
                    "name": str,
                    "surname": str,
                    "ID_Number": str,
                    "Birth_District": str,
                    "Image_url": str,
                    "status": int,
                },

        }
        return attributes

    def update(self, obj, idd, req_json, ignore_fields=[]):
        """
        :param ignore_fields: Fields that should not be updated
        :param req_json: json dictionary to update values (key,value) pairs
        :param idd: Item primary key
        :param obj: updates
        :return:
        """
        default_list_ignore = ["__class__", "created_at", "id", "updated_at" ]
        default_list_ignore += ignore_fields
        if obj:
            # update row to database
            row = self.__session.query(obj).filter_by(id=idd).first()
            # print("Result of no row results is ",row)
            if row:
                # print('original:', row.id, row.name)
                for key, value in req_json.items():
                    if key not in default_list_ignore:
                        setattr(row, key, value)
                setattr(row,"updated_at",datetime.datetime.utcnow())
                # self.updated_at = datetime.strptime( ["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                # self.updated_at =
                self.save()
                return row
            else:
                return None
        else:

            return None

    def ret_session(self):
        return self.__session
