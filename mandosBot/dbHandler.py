import sqlite3

def dbConnection():
    conn = None
    try:
        conn = sqlite3.connect('mandosBot.sqlite')
    except:
        print('Failed to connect to database.')
    return conn

conn = db_connection()

def createQuery(author, para, de, dmy1, dmy2 = None, price = 0):
    cursor = conn.cursor()
    sql = """INSERT INTO queries (
        author = ?,
        day_month_year1 = ?,
        day_month_year2 = ?,
        origin = ?,
        destiny = ?,
        price = ?
    )"""
    cursor.execute(sql, (author, para, de, dmy1, dmy2, price))
    cursor.close()
    return "Success!"

def acquire(author):
    cursor = conn.exxecute("""SELECT *
                              FROM queries
                              WHERE author = %s
                              """ % (author))
    cursor.close()
    pass

def delete():
    cursor = conn.cursor()
    cursor.close()
    pass

if __name__ == '__main__':
    conn = sqlite3.connect('mandosBot.sqlite')
    cursor = conn.cursor()
    sql_query = """ CREATE TABLE queries (
        id integer PRIMARY KEY,
        author text NOT NULL,
        day_month_year1 text NOT NULL,
        day_month_year2 text,
        origin text NOT NULL,
        destiny text NOT NULL,
        price integer NOT NULL
    )"""
    cursor.execute(sql_query)
    cursor.close()
    print('Success!')
