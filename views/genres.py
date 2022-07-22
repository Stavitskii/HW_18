from flask_restx import Resource, Namespace

genres_ns = Namespace('genres')


@book_ns.route('/')
class BooksView(Resource):
    def get(self):
        return "", 200

    def post(self):
        return "", 201
