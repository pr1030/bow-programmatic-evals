from dotenv import load_dotenv
import os

load_dotenv()

print("HOST =", os.getenv("DB_HOST"))
print("PORT =", os.getenv("DB_PORT"))
print("USER =", os.getenv("POSTGRES_USER"))
print("PASSWORD =", os.getenv("POSTGRES_PASSWORD"))
print("DATABASE =", os.getenv("POSTGRES_DB"))

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", "5432")),
    "database": os.getenv("POSTGRES_DB"),
    "user": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PASSWORD"),
}