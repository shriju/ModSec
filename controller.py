import logger as log
import pandas as pd

from models import model
import view

from database_operations.connection import Connection
from database_operations.db_operations import DatabaseOperations as db


# Get .csv Files, and put in model
for file_name in "regions,products,customers,sales".split(","):
    file_path = "data/"+file_name+".csv"
    model.frames.append(pd.read_csv(file_path))


# Create Empty Database
conn, cursor = Connection().make_connection()
db().db_create(conn, cursor)
conn.close()


# Populate Database from .csv Files
conn, cursor = Connection().make_connection(db_name = "sales_outlook")
db().db_populate(conn, cursor)


# Do 4 questions
question = view.Question()
for sql in question.sql.values():
    answer = model.get_data(cursor, sql)
    question.print_answer(answer)


conn.close() # close connection
