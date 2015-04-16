import fresh_tomatoes
import media

starwars_data = {"title": "Star Wars. Episode V: The Empire Strikes Back", "synopsis": "In the midst of a fierce lightsaber duel with the Sith Lord, Luke faces a startling revelation...", "poster_image_url": "http://pics.filmaffinity.com/Star_Wars_Episode_V_The_Empire_Strikes_Back-314829878-large.jpg", "trailer_youtube_url": "https://youtu.be/8Hm-9Sai9To", "score": 8.1}
clerks_data = {"title": "Clerks", "synopsis": "Dante Hicks is a clerk at a local convenience store in New Jersey", "poster_image_url": "http://pics.filmaffinity.com/Clerks-456270250-large.jpg", "trailer_youtube_url": "https://www.youtube.com/watch?v=Mlfn5n-E2WE", "score": 7.4}
rd_data = {"title": "Reservoir Dogs", "synopsis": "In the midst of a fierce lightsaber duel with the Sith Lord, Luke faces a startling revelation...", "poster_image_url": "http://pics.filmaffinity.com/Reservoir_Dogs-904905830-large.jpg", "trailer_youtube_url": "https://www.youtube.com/watch?v=GLPJSmUHZvU", "score": 8.2}
lotr_data = {"title": "The Lord of the Rings: The Fellowship of the Ring", "synopsis": "One ring to rule them all, One ring to find them. One ring to bring them all and in the darkness bind them", "poster_image_url": "http://pics.filmaffinity.com/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring-876628736-large.jpg", "trailer_youtube_url": "https://www.youtube.com/watch?v=aStYWD25fAQ", "score": 8.0}
snatch_data = {"title": "Snatch", "synopsis": "Turkish, an unlicenced boxing promoter is pulled into trouble when he becomes involved in big time criminal Brick Top, who wants him to arrange a fight and fix it", "poster_image_url": "http://pics.filmaffinity.com/Snatch-188547491-large.jpg", "trailer_youtube_url": "https://www.youtube.com/watch?v=lUloT3Dh3-E", "score": 7.9}

starwars = media.Movie(starwars_data)
clerks = media.Movie(clerks_data)
rd = media.Movie(rd_data)
lotr = media.Movie(lotr_data)
snatch = media.Movie(snatch_data)

mov =[starwars, clerks, lotr, rd, snatch]

fresh_tomatoes.open_movies_page(mov)

#for i in range(int(snatch.convert_rating())):
#	print '*'
