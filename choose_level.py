import mysql.connector


def get_data(cursor, table_name, difficulty):
    cursor.execute(f"SELECT * FROM {table_name}")
    result = cursor.fetchall()
    for x in result:
        if x[2] == difficulty:
            yield 'https://quera.org/' + x[1]


print('Choose difficulty:\n1)Easy\n2)Medium\n3)Hard')
chooser = {'1': 'ساده', '2': 'متوسط', '3': 'سخت'}
difficulty = chooser[input()]
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="43527681",
    database="quera"
)
for link in get_data(mydb.cursor(), 'questions', difficulty):
    print(link)
