from   resource_bus_logic import *

# Connection String
CNN = 'mssql+pyodbc://FONHST2SVR/ResourceDB?driver=SQL+Server+Native+Client+11.0'

def main():                                                     # Entry Point
    
    dbConnect(CNN)                                              # Connect to SQL Server

    print("\nBefore Insert Resource")
    rst = getResources()                                        # Get all Resources
    showData(rst)
    
    print("\nInsert Resource")
    addResource("Dina", "Bataq")                                # Append Resource to database

    print("\nAfter Insert Resource")
    rst = getResources()
    showData(rst)

    print("\nResource by Id")
    rst = getResourceById(3)                                    # Retrieve Resource By Id
    showData(rst)

    dbCommit()                                                 # Commit

    dbDisconnect()                                             # Disconnect

if __name__ == "__main__":

    main()
    print("\ndone")
    