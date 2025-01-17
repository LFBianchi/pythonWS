from flask import Flask, request, jsonify
app = Flask(__name__)

books_list = [
    {
        "id": 0,
        "author": "J. K. Rowling",
        "Language": "English",
        "title": "Harry Potter and the chamber of secrets"
    },
    {
        "id": 1,
        "author": "J. K. Rowling",
        "Language": "English",
        "title": "Harry Potter and the prisioner of Azkabhan"
    },
    {
        "id": 2,
        "author": "J. K. Rowling",
        "Language": "English",
        "title": "Harry Potter and the gobblet of fire"
    },
    {
        "id": 3,
        "author": "J. R. R. Tolkien",
        "Language": "English",
        "title": "The Hobbit"
    },
    {
        "id": 4,
        "author": "J. R. R. Tolkien",
        "Language": "English",
        "title": "The Silmarilon"
    }
]

@app.route('/books', methods = ['GET', 'POST'])
def books():
    if request.method == 'GET':
        if len(books_list) > 0:
            return jsonify(books_list)
        else:
            'Nothing Found', 404

    if request.method == 'POST':
        new_author = request.form['author']
        new_lang = request.form['Language']
        new_title = request.form['title']
        iD = books_list[-1]['id'] + 1

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
    if request.method == 'GET':
        for book in books_list:
            if book['id'] == id:
                return jsonify(book)
        else:
            return 'Nothing Found', 404
            pass
    if request.method == 'PUT':
        for book in books_list:
            if book['id'] == id:
                book['title'] = request.form['title']
                book['Language'] = request.form['Language']
                book['author'] = request.form['author']
                updated_book = {
                    'id': book['id'],
                    'Language': book['Language'],
                    'author': book['author'],
                    'title': book['title']
                }
                return jsonify(updated_book)
    if request.method == 'DELETE':
        for index, book in enumerate(books_list):
            if book['id'] == id:
                books_list.pop(index)
                return jsonify(books_list)

if __name__ == '__main__':
    app.run(debug = True)
