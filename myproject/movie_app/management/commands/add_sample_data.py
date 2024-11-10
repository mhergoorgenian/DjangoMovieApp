# myapp/management/commands/add_sample_data.py
from django.core.management.base import BaseCommand
from movie_app.models import MovieModel,AuthorModel,CategoryModel
import random

class Command(BaseCommand):
    help = "Add sample data with 3 authors, 3 categories, and 10 movies."

    def handle(self, *args, **kwargs):
        # Define authors
        authors_data = [
            {"name": "Christopher Nolan", "bio": "Director known for Inception and The Dark Knight."},
            {"name": "Steven Spielberg", "bio": "Famous for Jurassic Park and E.T."},
            {"name": "Quentin Tarantino", "bio": "Director of Pulp Fiction and Kill Bill."}
        ]

        # Define categories
        categories_data = [
            {"name": "Sci-Fi"},
            {"name": "Action"},
            {"name": "Drama"}
        ]

        # Define movies
        movies_data = [
            {"name": "Inception", "description": "A mind-bending thriller about dream infiltration.", "release_date": "2010-07-16", "rating": 8.8, "duration": 148},
            {"name": "Interstellar", "description": "An epic journey through space and time.", "release_date": "2014-11-07", "rating": 8.6, "duration": 169},
            {"name": "Jurassic Park", "description": "Dinosaurs brought back to life on a secluded island.", "release_date": "1993-06-11", "rating": 8.1, "duration": 127},
            {"name": "E.T.", "description": "A young boy befriends an alien stranded on Earth.", "release_date": "1982-06-11", "rating": 7.8, "duration": 115},
            {"name": "Pulp Fiction", "description": "Stories of crime in Los Angeles unfold in unique ways.", "release_date": "1994-10-14", "rating": 8.9, "duration": 154},
            {"name": "Kill Bill: Vol. 1", "description": "A revenge story with intense martial arts sequences.", "release_date": "2003-10-10", "rating": 8.1, "duration": 111},
            {"name": "Django Unchained", "description": "A freed slave sets out to rescue his wife from a brutal plantation owner.", "release_date": "2012-12-25", "rating": 8.4, "duration": 165},
            {"name": "The Dark Knight", "description": "Batman battles the Joker to save Gotham City.", "release_date": "2008-07-18", "rating": 9.0, "duration": 152},
            {"name": "Schindler's List", "description": "A businessman saves lives during the Holocaust.", "release_date": "1993-12-15", "rating": 9.0, "duration": 195},
            {"name": "Saving Private Ryan", "description": "A WWII squad embarks on a mission to save a paratrooper.", "release_date": "1998-07-24", "rating": 8.6, "duration": 169}
        ]

        # Create authors
        authors = []
        for author_data in authors_data:
            author, created = AuthorModel.objects.get_or_create(name=author_data["name"], bio=author_data["bio"])
            authors.append(author)

        # Create categories
        categories = []
        for category_data in categories_data:
            category, created = CategoryModel.objects.get_or_create(name=category_data["name"])
            categories.append(category)

        # Create movies
        for movie_data in movies_data:
            author = random.choice(authors)
            category = random.choice(categories)
            MovieModel.objects.get_or_create(
                name=movie_data["name"],
                description=movie_data["description"],
                author=author,
                category=category,
                release_date=movie_data["release_date"],
                rating=movie_data["rating"],
                duration=movie_data["duration"]
            )

        self.stdout.write(self.style.SUCCESS("Successfully added 3 authors, 3 categories, and 10 movies!"))
