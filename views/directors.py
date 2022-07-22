from flask_restx import Resource, Namespace

directors_ns = Namespace('directors')


@book_ns.route('/')
class BooksView(Resource):
    def get(self):
        return "", 200

    def post(self):
        return "", 201
