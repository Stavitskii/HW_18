from flask_restx import Resource, Namespace

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        return "", 200



@genre_ns.route('/<int:genre_id>')
class GenreView(Resource):
    def get(self, genre_id):
        return "", 200

