import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


class Conn:
    def __init__(self):
        uri = os.getenv("MONGODB_URI")
        if not uri:
            raise RuntimeError("MONGODB_URI is required to initialize database connection")

        self.client = MongoClient(uri)
        self.db = self.client["WebNote"]
        self.users = self.db["User"]
        self.notes = self.db["Note"]
