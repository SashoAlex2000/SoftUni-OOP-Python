from project import user
from project import movie_app
from project.movie_specification.thriller import Thriller

# test_user = user.User("Sasho", 22)
# print(test_user.username)
# test_user2 = User("", 22)
# test_user = User("Sasho", 1)
# test_thriller = Thriller("Django", 2013, test_user)
# test_user.movies_owned.append(test_thriller)
# test_user.movies_liked.append(test_thriller)
# print(test_user)

test_movie_app = movie_app.MovieApp()
# print(test_movie_app.users_collection)
print(test_movie_app.register_user("Sasho", 22))
# print(test_movie_app.users_collection)
# for user in test_movie_app.users_collection:
#     print(user)
test_user = test_movie_app.users_collection[0]
test_thriller = Thriller("Django", 2013, test_user)


# print(f"Printing who owns the movie: {test_thriller.owner}")
# print(test_movie_app.register_user("Sasho", 123))
print(test_movie_app.upload_movie("Sasho", test_thriller))
# print(test_movie_app.unpload_movie("Sasho", test_thriller))
print(test_movie_app.edit_movie("Sasho", test_thriller, title ="Djago"))
print(test_movie_app.edit_movie("Sasho", test_thriller, year =2011))
print(test_thriller.year)

test_thriller2 = Thriller("American Psycho", 2006, test_user)
test_thriller3 = Thriller("Morbius", 2022, test_user)
test_thriller4 = Thriller("Dr. Strange", 2022, test_user)
print(test_movie_app.upload_movie("Sasho", test_thriller2))
print(test_movie_app.upload_movie("Sasho", test_thriller3))
print(test_movie_app.upload_movie("Sasho", test_thriller4))
print(test_user.movies_owned)
print(test_movie_app.delete_movie("Sasho", test_thriller2))
# print(test_movie_app.delete_movie("Sasho", test_thriller2))
print(test_user.movies_owned)
# print(test_movie_app.like_movie("Sasho", test_thriller))
print(test_movie_app.register_user("Eli", 22))
test_user2 = test_movie_app.users_collection[1]
print(test_movie_app.like_movie("Eli", test_thriller))
# print(test_movie_app.like_movie("Eli", test_thriller))
print(test_movie_app.register_user("Djago", 22))
test_user3 = test_movie_app.users_collection[2]
print(test_movie_app.like_movie("Djago", test_thriller))
print(test_movie_app.like_movie("Djago", test_thriller3))
# print(test_movie_app.dislike_movie("Djago", test_thriller3))
print(test_thriller3)
print(test_movie_app.display_movies())
print(test_movie_app)

for movie in test_user3.movies_liked:
    print(movie.details())

print(test_movie_app.delete_movie("Sasho", test_thriller3))

for movie in test_user3.movies_liked:
    print(movie.details())