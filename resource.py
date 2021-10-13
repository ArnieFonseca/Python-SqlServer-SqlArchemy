""" Resource ORM"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Resource(Base):
    """ Rsource Class"""
    __tablename__ = 'resource'

    id = Column(Integer, primary_key=True, autoincrement=True)
    firstName = Column(String)
    lastName = Column(String)

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        