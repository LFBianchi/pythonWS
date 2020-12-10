from flask import Flask, request, jsonify
import sqlite3
import json

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('books.sqlite')
    except:
        print('Error, no database found.')
    return conn


@app.route('/books', methods = ['GET', 'POST'])
def books():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor = conn.execute('SELECT * FROM book')
        books = [
            dict(id = row[0], author = row[1], language = row[2], title = row[3])
            for row in cursor.fetchall()
        ]
        if books:
            return jsonify(books)

    if request.method == 'POST':
        new_author = request.form['author']
        new_lang = request.form['Language']
        new_title = request.form['title']
        sql = """INSERT INTO book (author, language, title)
                 VALUES (?, ?, ?)
                 """
        cursor.execute(sql, (new_author, new_lang, new_title))
        conn.commit()
        return f"Book with the id: {cursor.lastrowid} created succesfully!", 201

        new_obj = {
            'id': iD,
            'author': new_author,
            'Language': new_lang,
            'title': new_title
        }
        books_list.append(new_obj)
        return jsonify(books_list), 201


@app.route('/books/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
def single_book(id):
    conn = db_connection()
    cursor = conn.cursor()
    book = None

    if request.method == 'GET':
        cursor.execute("SELECT * FROM book WHERE id = ?", (id, ))
        rows = cursor.fetchall()
        for r in rows:
            book = r
        if book:
            return jsonify(book), 200
        else:
            return "Book not found.", 404

    if request.method == 'PUT':
        sql = """
              UPDATE book
              SET title = ?,
                  author = ?,
                  language = ?
              WHERE id = ?
              """
        author = request.form['author']
        language = request.form['Language']
        title = request.form['title']
        updated_book = {
                    'id': id,
                    'Language': language,
                    'author': author,
                    'title': title
                }
        conn.execute(sql, (title, language, author, id))
        conn.commit()
        return jsonify(updated_book)

    if request.method == 'DELETE':
        sql = """ DELETE FROM book WHERE id=? """
        conn.execute(sql, (id,))
        conn.commit()
        return f'Book with id: {id} has been deleted succesfully!'

if __name__ == '__main__':
    app.run(debug = True)
