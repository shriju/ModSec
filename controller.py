import logger as log
import view

from models.create_data import Create
from models import model

from database_operations.connection import Connection
from database_operations.db_operations import DatabaseOperations as db

import pandas as pd
#------------------------------importing complete-----------------------------------

Create().create()    # Create data

for file_name in "regions,products,customers,sales".split(","):    # Get .csv Files, and put in model
    file_path = "data/cleaned_data/" + file_name + ".csv"
    model.frames.append(pd.read_csv(file_path))


conn, cursor = Connection().make_connection()   # Create Empty Database
db().db_create(conn, cursor)
conn.close()


conn, cursor = Connection().make_connection(db_name = "sales_outlook")    # Populate Database from .csv Files
db().db_populate(conn, cursor)


question = view.Question()     # Do level_9's 1 to 4 questions
for sql in question.sql.values():
    answer = model.get_data(cursor, sql)
    question.print_answer(answer)


conn.close()    # close connection
log.f.close()   # close log file