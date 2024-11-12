# Django Movie API

This is a Django REST Framework (DRF) project for managing a movie database with CRUD operations on movies, authors, and categories. The app includes authentication, allowing only admins to create, update, or delete movies.

## Features

- **CRUD Operations** for Movies, Authors, and Categories
- **Authentication** with token for secure access
- **Admin Restrictions** on adding, updating, or deleting movies
- **Automated Tests** for all CRUD operations

## Project Structure

- **models.py**: Contains `Movie`, `Author`, and `Category` models.
- **views.py**: Defines views for creating, retrieving, updating, and deleting movies, authors, and categories.
- **serializers.py**: Serializers to handle JSON conversion.
- **tests.py**: Automated tests for CRUD operations.
- **urls.py**: Routes for accessing the API.

## Endpoints

The following endpoints are provided in this API:

### Authentication
- **POST /register**: Register a new user
- **POST /login**: Log in a user and receive a token

### Categories
- **GET /categories**: Retrieve all categories
- **POST /categories**: Create a new category (admin only)
- **GET /category/<id>**: Retrieve a category by ID
- **PUT /category/<id>**: Update a category by ID (admin only)
- **DELETE /category/<id>**: Delete a category by ID (admin only)

### Authors
- **GET /authors**: Retrieve all authors
- **POST /authors**: Create a new author (admin only)
- **GET /author/<id>**: Retrieve an author by ID
- **PUT /author/<id>**: Update an author by ID (admin only)
- **DELETE /author/<id>**: Delete an author by ID (admin only)

### Movies
- **GET /movies**: Retrieve all movies
- **POST /movies**: Create a new movie (admin only)
- **GET /movie/<id>**: Retrieve a movie by ID
- **PUT /movie/<id>**: Update a movie by ID (admin only)
- **DELETE /movie/<id>**: Delete a movie by ID (admin only)

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mhergoorgenian/DjangoMovieApp.git
   cd DjangoMovieApp
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Create a Superuser**:
   ```bash
   python manage.py createsuperuser
   ```

5. **Start the Server**:
   ```bash
   python manage.py runserver
   ```

## Running Tests

To run the automated tests, use the following command:

```bash
python manage.py test
```


