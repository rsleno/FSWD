import fresh_tomatoes
import media

clerks_data = {'title': 'Clerks', 'synopsis': 'Dante Hicks is a clerk at a local convenience store in New Jersey', 'poster_image_url': 'http://pics.filmaffinity.com/Clerks-456270250-large.jpg', 'trailer_youtube_url': 'https://www.youtube.com/watch?v=Mlfn5n-E2WE'}
rd_data = {'title': 'Reservoir Dogs', 'synopsis': 'In the midst of a fierce lightsaber duel with the Sith Lord, Luke faces a startling revelation...', 'poster_image_url': 'http://pics.filmaffinity.com/Reservoir_Dogs-904905830-large.jpg', 'trailer_youtube_url': 'https://www.youtube.com/watch?v=GLPJSmUHZvU'}
lotr_data = {'title': 'The Lord of the Rings: The Fellowship of the Ring', 'synopsis': 'One ring to rule them all, One ring to find them. One ring to bring them all and in the darkness bind them', 'poster_image_url': 'http://pics.filmaffinity.com/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring-876628736-large.jpg', 'trailer_youtube_url': 'https://www.youtube.com/watch?v=aStYWD25fAQ'}
snatch_data = {'title': 'Snatch', 'synopsis': 'Turkish, an unlicenced boxing promoter is pulled into trouble when he becomes involved in big time criminal Brick Top, who wants him to arrange a fight and fix it', 'poster_image_url': 'http://pics.filmaffinity.com/Snatch-188547491-large.jpg', 'trailer_youtube_url': 'https://www.youtube.com/watch?v=lUloT3Dh3-E'}

clerks = media.Movie(clerks_data)
rd = media.Movie(rd_data)
lotr = media.Movie(lotr_data)
snatch = media.Movie(snatch_data)

mov =[clerks, lotr, rd, snatch]

fresh_tomatoes.open_movies_page(mov)
