""" Calls Hellper"""
from enum import Enum, auto

SQL = """
        select id, firstName, lastname 
        from resource
    """
class Field(Enum):
    """ Table fields"""
    ID = 0
    FirstName = auto()
    LastName = auto()

class EmployeeHelper:
    def __init__(self, row) -> None:
        self.__id = row[Field.ID.value]
        self.__firstName = row[Field.FirstName.value]
        self.__lastname = row[Field.LastName.value]

    @property
    def ID(self):
        return self.__id

    @property
    def firstName(self):
        return self.__firstName
        
    @property
    def lastName(self):
        return self.__lastname
    
    @staticmethod
    def create_employee(row):
        return EmployeeHelper(row)
