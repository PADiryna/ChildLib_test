from flask import Flask, jsonify, abort, make_response, request, render_template
from models import books

app = Flask(__name__)
app.config["SECRET_KEY"] = "childbook"


@app.route("/", methods=["GET"])
def homepage():   
  return render_template("base.html")


@app.route('/book', methods=["GET"])
def books():
  items = books.all()
  return render_template("book.html", items=items)


@app.route("/book_info/<book_id>", methods=["GET"])
def get(book_id):
  bookdetails = books.get_book(book_id)
  name_button = "Hand out the book"
  if bookdetails[6]:
    name_button = "Return the book"
  if not bookdetails:
    abort(404)
  return render_template("book_info.html", title=bookdetails, name_button=name_button)


@app.route("/make_book", methods=["POST"])
def make_book():
  return render_template("make.html")


@app.route("/add_book", methods=["POST"])
def add_book():
  data = request.form  
  title = data.get('title')
  author = data.get('author')
  genre = data.get('genre')
  cover = data.get('cover')
  description = data.get('description')
  books.make(title, author, genre, cover, description)
  items = books.all()
  return render_template("book.html", items=items)


@app.errorhandler(404)
def not_found(error):
  return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)


@app.route("/delete_book/<int:book_id>", methods=['POST'])
def delete_book(book_id):
  result = books.delete(book_id)
  if not result:
    abort(404)
  items = books.all()
  return render_template("book.html", items=items)


@app.errorhandler(400)
def bad_request(error):
  return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)


if __name__ == "__main__":
  app.run(debug=True)