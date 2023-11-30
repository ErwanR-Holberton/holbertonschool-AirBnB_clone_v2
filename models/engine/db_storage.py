#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base


class DBStorage:
    """class for storage using mysql & alchemy"""
    __engine = None
    __session = None

    def __init__(self):
        """init msql db"""
        db_user = getenv('HBNB_MYSQL_USER')
        db_password = getenv('HBNB_MYSQL_PWD')
        db_host = getenv('HBNB_MYSQL_HOST')
        db_name = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                    .format(db_user, db_password, db_host,
                                            db_name), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        obj_dict = {}
        if cls is None:
            from models.user import User
            from models.place import Place
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.review import Review
            classes_list = [State, City]
            for class_i in classes_list:
                class_name = class_i.__name__
                for obj in self.__session.query(class_i).all():
                    key = "{}.{}".format(class_name, obj.id)
                    obj_dict[key] = obj
        else:
            for obj in self.__session.query(cls).all():
                obj_dict["{}.{}".format(type(obj), obj.id)] = obj
        return obj_dict

    def new(self, obj):
        """adds an object to the session"""
        self.__session.add(obj)

    def save(self):
        """save changes to the session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes an obj from the session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """close previous session and reopen"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))()
