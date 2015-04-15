
import urllib


class Movie():
	
	def __init__(self, movie_data):
		self.title = movie_data['title']
		self.synopsis = movie_data['synopsis']
		self.poster_image_url = movie_data['poster_image_url']
		self.trailer_youtube_url = movie_data['trailer_youtube_url']


	def show_trailer(self):
		utllib.open(self.youtube_url)


