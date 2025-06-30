from database import database
from models import basic_data

basic_data.Base.metadata.create_all(bind=database.engine)