
import urllib


class Movie():
	
	def __init__(self, movie_data):
		self.title = movie_data['title']
		self.synopsis = movie_data['synopsis']
		self.image_url = movie_data['image_url']
		self.youtube_url = movie_data['youtube_url']


	def show_trailer(self):
		utllib.open(self.youtube_url)


