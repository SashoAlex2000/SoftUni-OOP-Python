# START
from project.user import User
from project.movie_specification.movie import Movie


class MovieApp():
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username, age):
        current_user = User(username, age)
        # if current_user not in self.users_collection:
        #     self.users_collection.append(current_user)
        #     return f"{username} registered successfully."

        for user in self.users_collection:
            if user.username == username:
                raise Exception("User already exists!")

        self.users_collection.append(current_user)
        return f"{username} registered successfully."

        # User already exists!

    def upload_movie(self, username, movie: Movie):
        user_exists = False
        for user in self.users_collection:
            if user.username == username:
                user_exists = True

        if not user_exists:
            raise Exception("This user does not exist!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        for user in self.users_collection:
            if user.username == username:
                if movie.owner != user:
                    raise Exception(f"{username} is not the owner of the movie {movie.title}!")

                user.movies_owned.append(movie)
                self.movies_collection.append(movie)
                return f"{username} successfully added {movie.title} movie."

        # raise Exception("This user does not exist!")

    def edit_movie(self, username, movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        current_user = None
        for user in self.users_collection:
            if user.username == username:
                current_user = user

        if movie.owner != current_user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key, value in kwargs.items():
            attribute_to_edit = key
            # print(attribute_to_edit)
            movie.attribute_to_edit = value
            if key == "title":
                movie.title = value
            if key == "year":
                movie.year = value
            if key == "age_restriction":
                movie.age_restriction = value

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username, movie):

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        current_user = None
        for user in self.users_collection:
            if user.username == username:
                current_user = user

        if movie.owner != current_user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        current_user.movies_owned.remove(movie)

        for user in self.users_collection:
            if movie in user.movies_liked:
                user.movies_liked.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username, movie):
        current_user = None
        for user in self.users_collection:
            if user.username == username:
                current_user = user

        if movie.owner == current_user:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in current_user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        current_user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username, movie):
        current_user = None
        for user in self.users_collection:
            if user.username == username:
                current_user = user

        if movie not in current_user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        current_user.movies_liked.remove(movie)

        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if len(self.movies_collection) == 0:
            return "No movies found."

        sorted_list = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        result = ""

        for movie in sorted_list:
            if sorted_list.index(movie) < len(sorted_list) - 1:
                result += f"{movie.details()}\n"
            else:
                result += f"{movie.details()}"

        return result

    def __str__(self):
        result = ""
        if len(self.users_collection) > 0:
            result += f"All users: {', '.join(user.username for user in self.users_collection)}\n"
        else:
            result += "All users: No users.\n"

        if len(self.movies_collection) > 0:
            result += f"All movies: {', '.join(movie.title for movie in self.movies_collection)}"
        else:
            result += "All movies: No movies."

        return result

