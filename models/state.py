#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
import models

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')

    @property
    def cities(self):
        my_list = []
        my_dict = storage.all('City')
        for key, value in my_dict.items():
            if self.id == city.state_id:
                my_list.append(value)
        return my_list
