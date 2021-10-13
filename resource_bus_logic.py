from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from resource import Resource

session = None

def dbConnect(cnnStr):
    engine = create_engine(cnnStr, echo=False)                      # SQL Alchemy setup Engine and Session
    Session = sessionmaker(bind=engine)

    global session
    session = Session()

def showData(result):
    for item in result:
        print(f"{item.id} -> {item.lastName}, {item.firstName}")
        
def getResources():
    return session.query(Resource).all()
   
def getResourceById(id):
    return session.query(Resource).filter(Resource.id == id)

def addResource(firstName, lastName):
    resource = Resource(firstName=firstName, lastName=lastName) # Create new instance of the Resource
    session.add(resource)                                       # Add to the database

def dbCommit():
    session.commit()                                           # Commit action

def dbDisconnect():
    session.close()                                           # Close connection