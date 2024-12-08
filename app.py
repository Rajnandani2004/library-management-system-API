from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# In-memory database for books (just for testing)
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "1984", "author": "George Orwell"}
]

# GET all books
@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books)

# POST a new book
@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()
    title = data.get("title")
    author = data.get("author")
    if not title or not author:
        abort(400, "Missing title or author")
    new_book = {"id": len(books) + 1, "title": title, "author": author}
    books.append(new_book)
    return jsonify(new_book), 201

# GET a specific book by ID
@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book is None:
        abort(404, "Book not found")
    return jsonify(book)

# PUT (update) a book
@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book is None:
        abort(404, "Book not found")
    
    data = request.get_json()
    book["title"] = data.get("title", book["title"])
    book["author"] = data.get("author", book["author"])
    
    return jsonify(book)

# DELETE a book
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    global books
    books = [b for b in books if b["id"] != book_id]
    return '', 204  # No content

if __name__ == "__main__":
    app.run(debug=True)
