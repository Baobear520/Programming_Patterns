"""Implementing Dependency Injection in Python"""

from abc import ABC, abstractmethod
from typing import Any


class Database(ABC):
    def __init__(self, db_string: str):
        self.db_str = db_string
        self._is_connected = False

    @abstractmethod
    def connect(self) -> None:
        """Establish database connection"""
        pass

    @abstractmethod
    def disconnect(self) -> None:
        """Close database connection"""
        pass

    @abstractmethod
    def execute_query(self, query: str) -> Any:
        """Execute a database query"""
        pass

    @property
    def is_connected(self) -> bool:
        """Database connection status check"""
        return self._is_connected


class Service(ABC):
    def __init__(self, db: Database) -> None:
        self.db = db

    @abstractmethod
    def process_data(self) -> None:
        """Process data using the database"""
        pass


class PostgresDB(Database):
    def connect(self) -> None:
        if not self._is_connected:
            try:
                print(f"Connecting to {self.db_str}...")
                # Actual connection logic would go here
                self._is_connected = True
            except Exception as e:
                raise ConnectionError(f"Failed to connect to database: {str(e)}")

    def disconnect(self) -> None:
        if self._is_connected:
            try:
                print(f"Disconnecting from {self.db_str}...")
                # Actual disconnection logic would go here
                self._is_connected = False
            except Exception as e:
                raise ConnectionError(f"Failed to disconnect from database: {str(e)}")

    def execute_query(self, query: str) -> Any:
        if not self._is_connected:
            raise ConnectionError("Not connected to database")
        try:
            print(f"Executing query: {query}")
            # Actual query execution would go here
            return {"result": "dummy data"}
        except Exception as e:
            raise Exception(f"Query execution failed: {str(e)}")


class UserService(Service):
    def process_data(self) -> None:
        try:
            self.db.connect()
            result = self.db.execute_query("SELECT * FROM users")
            print(f"Processing user data: {result}")
        finally:
            self.db.disconnect()


class Application:
    def __init__(self, service: Service) -> None:
        self.service = service

    def run(self) -> None:
        try:
            self.service.process_data()
        except Exception as e:
            print(f"Application error: {str(e)}")


def main() -> None:
    try:
        db = PostgresDB("postgresql://localhost:5432/mydb")
        service = UserService(db=db)
        app = Application(service=service)
        app.run()
    except Exception as e:
        print(f"Failed to initialize application: {str(e)}")


if __name__ == "__main__":
    main()
