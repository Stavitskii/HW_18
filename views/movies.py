from flask_restx import Resource, Namespace

movie_ns = Namespace('movies')

@movie_ns.route('/')
class MovieView(Resource):
    def get(self):
        good_movie_query = db.session.query(Movie.id, Movie.title, Movie.description, Movie.rating, Movie.trailer,
                                            Genre.name.label('genre'), Director.name.label('director')).join(
            Genre).join(Director)

        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        if director_id:
            good_movie_query = good_movie_query.filter(Movie.director_id == director_id)
        if genre_id:
            good_movie_query = good_movie_query.filter(Movie.genre_id == genre_id)





        all_movies = good_movie_query.all()
        return movies_schema.dump(all_movies), 200

    def post(self):
        # функцию проверял на постмене, не заработала... Не могу понять, почему
        req_json = request.json
        new_movie = Movie(**req_json)
        with db.session.begin():
            db.session.add(new_movie)
        return f"An object is added", 201


@movie_ns.route('/<int:movie_id>')
class MovieView(Resource):
    def get(self, movie_id: int):
        good_movie_query = db.session.query(Movie.id, Movie.title, Movie.description, Movie.rating, Movie.trailer,
                                            Genre.name.label('genre'), Director.name.label('director')).join(
            Genre).join(Director)
        movie = good_movie_query.first()
        if movie:
            return movie_schema.dump(movie)
        else:
            return f"Movie {movie_id} is not found", 404

    def patch(self, movie_id):
        movie = db.session.query(Movie).get(movie_id)
        req_json = request.json
        if 'title' in req_json:
            movie.title = req_json['title']
        elif 'description' in req_json:
            movie.description = req_json['description']
        elif 'trailer' in req_json:
            movie.trailer = req_json['trailer']
        elif 'year' in req_json:
            movie.year = req_json['year']
        elif 'rating' in req_json:
            movie.rating = req_json['rating']
        elif 'genre_id' in req_json:
            movie.genre_id = req_json['genre_id']
        elif 'director_id' in req_json:
            movie.director_id = req_json['director_id']
        db.session.add(movie)
        db.session.commit()
        return f"An object with id {movie_id} is patched", 204

    def put(self, movie_id):
        movie = db.session.query(Movie).get(movie_id)
        if not movie:
            return "Not a movie found", 404
        req_json = request.json

        movie.title = req_json['title']
        movie.description = req_json['description']
        movie.trailer = req_json['trailer']
        movie.year = req_json['year']
        movie.rating = req_json['rating']
        movie.genre_id = req_json['genre_id']
        movie.director_id = req_json['director_id']

        db.session.add(movie)
        db.session.commit()
        return f"An object with id {movie_id} is patched", 204

    def delete(self, movie_id):
        movie = db.session.query(Movie).get(movie_id)
        if not movie:
            return "Not a movie found", 404
        db.session.delete(movie)
        db.session.commit()
        return f"An object with id {movie_id} is deleted", 204

