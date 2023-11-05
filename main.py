from flask import Flask

from .database.connection import *
from .import create_app
app = Flask(__name__)

app = create_app()

try:
    db = initialize_db()
    connection = db.connect()

    Session = sessionmaker(bind=db)
    session = Session()

except ValueError as e:
    print(e)