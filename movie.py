import fresh_tomatoes
import media

starwars_data = {'title': 'Star Wars. Episode V: The Empire Strikes Back', 'synopsis': 'In the midst of a fierce lightsaber duel with the Sith Lord, Luke faces a startling revelation...', 'poster_image_url': 'http://pics.filmaffinity.com/Star_Wars_Episode_V_The_Empire_Strikes_Back-314829878-large.jpg', 'trailer_youtube_url': 'https://www.youtube.com/watch?v=JNwNXF9Y6kY'}

starwars = media.Movie(starwars_data)
mov =[starwars, starwars, starwars, starwars, starwars, starwars]

fresh_tomatoes.open_movies_page(mov)
