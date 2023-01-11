from pymongo import MongoClient

# Base de datos local
# db_client = MongoClient().local

# Base de datos cloud
db_client = MongoClient("mongodb+srv://Camilo:Samimajo10@cluster0.n37cpaj.mongodb.net/?retryWrites=true&w=majority").test