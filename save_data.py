import csv
import os

import mysql.connector


def from_file_to_database(path, database, table_name):
    cursor = database.cursor
    to_be_inserted = []
    with open(path) as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            to_be_inserted.append(tuple(line))
    sql = f"INSERT INTO {table_name} (name, link, level) VALUES (%s, %s, %s)"
    cursor.executemany(sql, to_be_inserted)
    database.commit()


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="43527681",
    database="quera"
)
file_path = os.path.join(os.getcwd(), 'collector/data.csv')
from_file_to_database(file_path, mydb, 'questions')
