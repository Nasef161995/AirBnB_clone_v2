#!/usr/bin/python3
"""This module defines a class to manage DB Storage for hbnb clone"""
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv

class DBStorage:
    __engine = None
    __session = None
    def __init__(self):
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                           format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB),
                           pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
