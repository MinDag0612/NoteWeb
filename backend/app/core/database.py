import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://127.0.0.1:27017")


class Conn:
    def __init__(self):
        self.client = MongoClient(MONGODB_URI)
        self.db = self.client["WebNote"]
        self.users = self.db["User"]
        self.notes = self.db["Note"]


connDB = Conn()