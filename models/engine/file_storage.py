#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import datetime


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            dictionary = dict()
            for item in FileStorage.__objects.items():
                if type(item[1]) in [cls]:
                    dictionary[item[0]] = item[1]
                else:
                    continue
            return dictionary

        else:
            return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.city import City
        from models.Collection_Stations import Kitambulisho_Collection_Station
        from models.collector_signoff import Kitambulisho_Collection_Station_SignOff
        from models.Counties import County
        from models.Kitambulisho_Collection_Register import Kitambulisho_Collection_Register
        from models.review import Review
        from models.user import User
        from models.vitambulisho import Kitambulisho

        classes = {
            'BaseModel': BaseModel,
            'City': City,
            'Kitambulisho_Collection_Station': Kitambulisho_Collection_Station,
            'Kitambulisho_Collection_Station_SignOff': Kitambulisho_Collection_Station_SignOff,
            'County': County,
            'Kitambulisho_Collection_Register': Kitambulisho_Collection_Register,
            'Review': Review,
            'User': User,
            'Kitambulisho': Kitambulisho,
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

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

    def delete(self, obj=None):
        """ Deletes Obj from __objects Global storage Dictionary
        parameters:
        obj [class object] - object to be deleted
        returns: true on success else false
        """
        if obj:

            key = obj.to_dict()['__class__'] + '.' + obj.id
            try:
                del (self.__objects[key])
                self.save()
                return True
            except BaseException:
                return False
                pass
            # del(self.all()[key])
        else:
            return True
            pass

    def close(self):
        """
            calls the reload() method for deserialization from JSON to objects
        """
        self.reload()

    def get(self, cls=None, id=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            for item in FileStorage.__objects.items():
                if type(item[1]) in [cls]:
                    key = str(cls.__name__) + '.' + id
                    # print(key)
                    return self.__objects.get(key, None)
                    break
                else:
                    continue
            return None

        else:
            return FileStorage.__objects

    def count(self, cls=None):
        """
        :param cls:  Defines the Class to which its instance objects to count
        :return: a +ve integer value else zero
        """
        count = 0
        if cls:
            for item in FileStorage.__objects.items():
                if type(item[1]) in [cls]:
                    count += 1
                else:
                    continue
            return count

        else:
            return len(FileStorage.__objects)

    def update(self, obj, idd, req_json, ignore_fields=[]):
        """
        :param req_json: json dictionary
        :param idd:
        :param obj: updates
        :return:
        """
        default_list_ignore = ["__class__", "created_at", "id", "updated_at"]
        default_list_ignore += ignore_fields
        if obj:

            pkey = "{}.{}".format(obj.__name__, idd)

            for key, value in req_json.items():
                if key not in default_list_ignore:
                    try:
                        setattr(self.__class__.__objects[pkey], key, value)
                    except BaseException:
                        return None
            setattr(self.__class__.__objects[pkey], "updated_at", datetime.datetime.utcnow())
            self.save()
            self.reload()
            return self.__class__.__objects[pkey]
        else:

            return None
