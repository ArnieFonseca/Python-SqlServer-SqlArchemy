import pymssql._pymssql as db
import resource_helper as emp

cnn = db.connect(host='FONHST2SVR', database='ResourceDB')

cursor = cnn.cursor()

cursor.execute(emp.SQL)

data = cursor.fetchall()

for row in data:
    employee = emp.EmployeeHelper.create_employee(row)
    print(f"{employee.ID} -> {employee.firstName}, {employee.lastName}")

cursor.close()
cnn.close()

