import pymssql._pymssql as db
import employee_helper as emp

cnn = db.connect(host='FONHST2SVR', database='Demo')

cursor = cnn.cursor()

cursor.execute(emp.SQL)

data = cursor.fetchall()

for row in data:
    employee = emp.EmployeeHelper.create_employee(row)
    print(f"{employee.ID} -> {employee.Name}, {employee.Department}")

cursor.close()
cnn.close()

