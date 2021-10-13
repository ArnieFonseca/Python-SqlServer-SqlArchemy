""" Calls Hellper"""
from enum import Enum, auto

SQL = """
        SELECT e.Id, e.Name, d.Name DeptName 
        FROM   DM.Employees e
        INNER JOIN DM.Departments d
        ON e.DepartmentId = d.Id
        ORDER BY d.Name, e.Name
    """
class Field(Enum):
    """ Table fields"""
    ID = 0
    Name = auto()
    Department = auto()

class EmployeeHelper:
    def __init__(self, row) -> None:
        self._id = row[Field.ID.value]
        self._name = row[Field.Name.value]
        self._department = row[Field.Department.value]

    @property
    def ID(self):
        return self._id

    @property
    def Name(self):
        return self._name
        
    @property
    def Department(self):
        return self._department
    
    @staticmethod
    def create_employee(row):
        return EmployeeHelper(row)
