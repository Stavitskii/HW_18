from flask_restx import Resource, Namespace

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        return "", 200



@genre_ns.route('/<int:director_id>')
class DirectorView(Resource):
    def get(self, director_id):
        return "", 200

