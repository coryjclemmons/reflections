import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy with his toys",
                        "toystory.jpg",
                        "http://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwitloicgcvMAhUQ1mMKHYQMAZIQyCkIHjAA&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DKYz2wyBy3kc&usg=AFQjCNEJoSlxDJtzDTMi_7zEW-AOc2Z4MA&sig2=2bYpg2ZvW-BenWRwXUn3lQ&bvm=bv.121421273,d.cGc")


avatar = media.Movie("Avitar",
                     "A story of an alien",
                     "avitar.jpg",
                     "http://www.imdb.com/video/imdb/vi531039513?ref_=tt_ov_vi")

godfather = media.Movie("Godfather",
                     "A story of an officer and his father",
                     "godfather.jpg",
                    "https://www.youtube.com/watch?v=G9C59wgq2A8")

#print(media.Movie.VALID_RATINGS)

#movies = [toy_story, avatar, godfather]

#fresh_tomatoes.open_movies_page(movies)

print(media.Movie.__name__)

print(media.Movie.__module__)
