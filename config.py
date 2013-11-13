import os

# Just a friendly reminder, DO NOT SET secret keys / passwords in this file. 
# Instead use environment variables like shown with DATABASE_URL
DB_URI = os.environ.get("DATABASE_URL", "sqlite:///my_app.db")
SECRET_KEY = "this should be a secret"
