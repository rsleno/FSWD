import fresh_tomatoes
import media

movie_data = [
{"title": "Star Wars. Episode V", "year": "1980" , "synopsis": "In the midst of a fierce lightsaber duel with the Sith Lord, Luke faces a startling revelation...", "poster_image_url": "http://pics.filmaffinity.com/Star_Wars_Episode_V_The_Empire_Strikes_Back-314829878-large.jpg", "trailer_youtube_url": "https://youtu.be/8Hm-9Sai9To", "score": 8.1},
{"title": "Clerks", "year": "1994" , "synopsis": "Dante Hicks is a clerk at a local convenience store in New Jersey", "poster_image_url": "http://pics.filmaffinity.com/Clerks-456270250-large.jpg", "trailer_youtube_url": "https://www.youtube.com/watch?v=Mlfn5n-E2WE", "score": 7.4},
{"title": "Reservoir Dogs", "year": "1992" , "synopsis": "In the midst of a fierce lightsaber duel with the Sith Lord, Luke faces a startling revelation...", "poster_image_url": "http://pics.filmaffinity.com/Reservoir_Dogs-904905830-large.jpg", "trailer_youtube_url": "https://www.youtube.com/watch?v=GLPJSmUHZvU", "score": 8.2},
{"title": "The Lord of the Rings", "year": "2001" , "synopsis": "One ring to rule them all, One ring to find them. One ring to bring them all and in the darkness bind them", "poster_image_url": "http://pics.filmaffinity.com/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring-876628736-large.jpg", "trailer_youtube_url": "https://www.youtube.com/watch?v=aStYWD25fAQ", "score": 8.0},
{"title": "Snatch", "year": "2000" , "synopsis": "Turkish, an unlicenced boxing promoter is pulled into trouble when he becomes involved in big time criminal Brick Top, who wants him to arrange a fight and fix it", "poster_image_url": "http://pics.filmaffinity.com/Snatch-188547491-large.jpg", "trailer_youtube_url": "https://www.youtube.com/watch?v=lUloT3Dh3-E", "score": 7.9},
{"title": "Birdman", "year": "2014", "synopsis": "A washed up actor who once played an iconic superhero must overcome his ego and family trouble as he prepares to mount a Broadway play in a bid to reclaim past glory.", "poster_image_url": "http://pics.filmaffinity.com/Birdman-594952048-large.jpg", "trailer_youtube_url": "https://www.youtube.com/watch?v=xIxMMv_LD5Q", "score": 7.2},
{"title": "Interstellar", "year": "2014", "synopsis": "In the near future Earth has been devastated by drought and famine, causing a scarcity in food and extreme changes in climate.", "poster_image_url": "http://pics.filmaffinity.com/Interstellar-366875261-large.jpg", "trailer_youtube_url": "https://www.youtube.com/watch?v=zSWdZVtXT7E", "score": 7.8},
{"title": "The Godfather", "year": "1972", "synopsis": "Epic tale of a 1940s New York Mafia family and their struggle to protect their empire from rival families as the leadership switches from the father to his youngest son.", "poster_image_url": "http://pics.filmaffinity.com/The_Godfather-485345341-large.jpg", "trailer_youtube_url": "https://www.youtube.com/watch?v=1aV9X2d-f5g", "score": 9.1}
]

mov = []

for m in movie_data:
	mov.append(media.Movie(m))


fresh_tomatoes.open_movies_page(mov)

#for i in range(int(snatch.convert_rating())):
#	print '*'
