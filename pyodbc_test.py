import pyodbc

cnn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=FONHST2SVR;"
            "Database=ResourceDB;"
            "Trusted_Connection=yes;")

cnn = pyodbc.connect(cnn_str)

cursor = cnn.cursor()
rows = cursor.execute("select * from resource where id > 2")

for row in rows:
    print(row)

cursor.close()

cnn.close()