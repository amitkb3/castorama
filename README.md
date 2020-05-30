# Casting Agency Capstone Project

This project is to fulfil Capstone project requirements for the Full-Stack Developer Nanodegree Program at Udacity.
**Heroku link:** (https://castorama.herokuapp.com/)

## Project Background 
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. 

This api is responsible for creating a system to simplify and streamline your process. It provides CURD operations for management of actors and movies. It also enable role based access controls (RBAC) via Auth0.

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the root directory of this project and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

After installing the dependencies, execute the bash file `setup.sh` to set the user jwts, auth0 credentials and the remote database url by naviging to the root directory of this project and running:

```bash
source setup.sh
```

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the root directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
source setup.sh
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

The Environment variables are saved in `SETUP.SH` file. The following environment variables are set as shown is the example file `SETUP_EXAMPLE.SH`
* SECRET_KEY - Secret key for flask app
* DATABASE_URL - postgres URI for the app database
* TEST_DATABASE_URL - postgres URI for the app test database
* AUTH0_DOMAIN - Auth0 domain
* API_AUDIENCE - Auth0 api audience
* ASSISTANT_JWT - token for casting assistant role
* DIRECTOR_JWT - token for casting director role
* PRODUCER_JWT - token for executive producer role

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `app.py` directs flask to use the `app.py` file to find the application. 

## API Reference

### Endpoints

#### GET '/actors'
- Gets list of actors
- Requires role with permission `get:actor`
- Request Arguments: None
- Returns: list of actors
```

{
  'success': True,
  'actors': [
    {
      id: 1,
      name: 'actor1',
      age: 30,
      gender: 'F'
    }
  ]
}
```

#### GET '/movies'
- Gets a list of movies.
- Requires role with permission `get:movies`
- Request Arguments: None
- Returns: list of movies.
```
{
  'success': True,
  'movies': [
    {
      id: 1,
      title: 'movie1',
      release_date: '2020-05-27 21:36:09'
    }
  ]
}
```

#### POST '/actors'
- Create a new actor.
- Requires role with permission `post:actor`
- Request Arguments: { name: String, age: Integer, gender: String }.
- Returns: the details of the new actor added.
```
{
  'success': True,
  'actors': [
    {
      id: 2,
      name: 'actor2',
      age: 35,
      gender: 'M'
    }
  ]
}
```

#### POST '/movies'
- Create a new movie.
- Requires role with permission `post:Movies`
- Request Arguments: { title: String, release_date: DateTime }.
- Returns: the details of new movie added.
```
{
  'success': True,
  'movies': [
    {
      id: 2,
      title: 'movie2',
      release_date: '2020-05-27 21:36:23'
    }
  ]
}
```

#### Patch '/actors/<actor_id>'
- Update an actor.
- Requires role with permission `patch:actor`
- Request Arguments: { name: String, age: Integer, gender: String }.
- Returns: Details of updated actor.
```
{
  'success': True,
  'actors': [
    {
      id: 1,
      name: 'actor2',
      age: 40,
      gender: 'F'
    }
  ]
}
```

#### Patch '/movies/<movie_id>'
- Update a movie.
- Requires role with permission `patch:Movies`
- Request Arguments: { title: String, release_date: DateTime }.
- Returns: Details of updated movie.
```
{
  'success': True,
  'movies': [
    {
      id: 1,
      title: 'movie1',
      release_date: '2020-05-27 21:36:09'
    }
  ]
}
```

#### DELETE '/actors/<actor_id>'
- Removes an actor from the database.
- Requires role with permission `delete:actor`
- Request Parameters: actor id parameter.
- Returns: the id of the deleted actor
```
{
  'success': True,
  'id': 1
}
```

#### DELETE '/movies/<movie_id>'
- Removes a movie from the database.
- Requires role with permission `delete:movies`
- Request Parameters: question id parameter.
- Returns: the id of the deleted movie
```
{
  'success': True,
  'id': 1
}
```
### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 404,
    "message": "not found."
}
```
## Testing

#### Running tests locally
To run the tests from ./test_app.py, first make sure you have ran and executed the setup.sh file to set the enviorment.

After setting the enviorment start your local postgress server:
```bash
pg_ctl -D /usr/local/var/postgres start
```

Then run the follwing commands to run the tests:
```
dropdb casting_test
createdb casting_test
psql casting_test < casting_test.psql
python test_app.py
```
