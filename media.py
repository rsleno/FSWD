import webbrowser


class Movie():
	""" This class stores movie information.

	Attributes:
        title: A string with the movie title.
        year: A string with the release year of the movie.
        synopsis: A string with the synopsis of the movie.
        poster_image_url: A string with the url of the movie poster.
        trailer_youtube_url: A string with the youtube url of the movie trailer.
        score: Float with the movie rating score.
	"""
	
	def __init__(self, movie_data):
		""" Inits the Movie Class. """
		self.title = movie_data['title']
		self.year = movie_data['year']
		self.synopsis = movie_data['synopsis']
		self.poster_image_url = movie_data['poster_image_url']
		self.trailer_youtube_url = movie_data['trailer_youtube_url']
		self.score = movie_data['score']


	def convert_rating(self):
		""" Converts float score in base 10 to a rounded integer in base 5. """
		return int(round(self.score / 2))


