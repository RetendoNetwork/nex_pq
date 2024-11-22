class DatabaseError(Exception):
    pass

class ConnectionError(DatabaseError):
    pass

class CreateDatabaseError(DatabaseError):
    pass

class CreateTableError(DatabaseError):
    pass

class InsertDataError(DatabaseError):
    pass