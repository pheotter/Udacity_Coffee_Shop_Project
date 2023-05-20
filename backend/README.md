# Coffee Shop Backend
All backend code follows [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/).
## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py
export FLASK_DEBUG=1
flask run
```

Setting the FLASK_DEBUG variable to true means that we are working in development mode and it shows an interactive debugger in the console and restarts the server whenever changes are made.

The application is run on http://127.0.0.1:5000/ by default.

## Tasks

### Setup Auth0

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
   - in API Settings:
     - Enable RBAC
     - Enable Add Permissions in the Access Token
5. Create new API permissions:
   - `get:drinks`
   - `get:drinks-detail`
   - `post:drinks`
   - `patch:drinks`
   - `delete:drinks`
6. Create new roles for:
   - Barista
     - can `get:drinks-detail`
     - can `get:drinks`
     - User: coffee_barista@udacity.com
     - Password: @udacity987
     - JWT `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxuUEp4X0lYQ3pVTVdwU3drU3kzVSJ9.eyJpc3MiOiJodHRwczovL2Rldi1uNnBodDh1enI3OHpkbmx4LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDU4ZWM4NDBhZjJkMDU4MmU1ZDFlZmEiLCJhdWQiOiJjb2ZmZWUiLCJpYXQiOjE2ODQ1NDgyNzIsImV4cCI6MTY4NDU1NTQ3MiwiYXpwIjoieURDNGJQR2hyUFZrYVBHaXpXY2VqVmlHeDBrZFJQb1QiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpkcmlua3MiLCJnZXQ6ZHJpbmtzLWRldGFpbCJdfQ.f2f9L9B31wKHj9KqTRRkU-TtPbf92zLQsjaywv9ObnVLpv1ppvretDPJyFtKPDvcn8xgFfpkuUxXAOig-V0UEbD7kilDfM5S-u981G00gwUGDBwuKVCuOU-kfg7HWJWlb3cbWUaeHjUIuHWjYTG_ti6Wmbj6R1cqI29XR4dJcZD6vsoopmN7m0lBDONB585og1b1o693N5HqfiC03MPXYQP3Z4WUC6w5K6pwHfw2G02BcN9Ni8ACKAeccu3hT6FgYycCB-BW0uJExAMqOM_TNkbK3l9yo6qeJH6wF0mg7Geezyh3ctZzU3gKU8IhyyI45ht7gc4u3Z-pFabrJSRS-Q`
   - Manager
     - can perform all actions
     - User: coffee_manager@udacity.com
     - Password: @udacity987
     - JWT `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxuUEp4X0lYQ3pVTVdwU3drU3kzVSJ9.eyJpc3MiOiJodHRwczovL2Rldi1uNnBodDh1enI3OHpkbmx4LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDU4ZTkzMzBhZjJkMDU4MmU1ZDFlOGQiLCJhdWQiOiJjb2ZmZWUiLCJpYXQiOjE2ODQ1NDgzMTgsImV4cCI6MTY4NDU1NTUxOCwiYXpwIjoieURDNGJQR2hyUFZrYVBHaXpXY2VqVmlHeDBrZFJQb1QiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpkcmlua3MiLCJnZXQ6ZHJpbmtzIiwiZ2V0OmRyaW5rcy1kZXRhaWwiLCJwYXRjaDpkcmlua3MiLCJwb3N0OmRyaW5rcyJdfQ.U7PzzFVuTeWNesDgrFxIjTToHYPaO_kBSxmO_huf_0jXYIqeJAbuOkmdQwudUctcDGsQMxGfHRV_H7RWt0m_BrBZCqiQW2JuFJL9MrViMz8cZThk8Xao_YdCzE6wrqyT9izRKDAKkekqoWatj13f5J5MEKRZc8xKIAGkKb4uVtPlGjHQtHeFKJ95Y5Eypaa95Ppz6HeKlDYCiz0STcqMaF1mLLt67_0NR-GXRUUCt7wBksX5JGSLzIoJYBWiS52dHZhLOM0mLUwygtvi6fzLoV96zf5uWlm85HuEnoYccWk1in7zW5T9ybuWLlLb9pttidszzsn-PbYYfB8mcl08Eg`
7. Test your endpoints with [Postman](https://getpostman.com).
   - Register 2 users - assign the Barista role to one and Manager role to the other.
   - Sign into each account and make note of the JWT.
   - Import the postman collection `./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`
   - Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
   - Run the collection and correct any errors.
   - Export the collection overwriting the one we've included so that we have your proper JWTs during review!
   - My test results containing 20 successful cases: `/backend/udacity-fsnd-udaspicelatte.postman_collection_result.json`

### Implement The Server

There are `@TODO` comments throughout the `./backend/src`. We recommend tackling the files in order and from top to bottom:

1. `./src/auth/auth.py`
2. `./src/api.py`

## API Reference
### Getting Started
- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:5000/`
- Authentication: using Auth0.

### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False,
    "error": 400,
    "message": "bad request"
}
```
The API will return seven error types when requests fail:
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Resource Not Found
- 405: Method Not Allowed
- 422: Not Processable
- 500: Internal Server Error

### Endpoints
#### GET /drinks
- General:
    - Returns a success value, a list of available drinks with brief description.
- Sample: `curl http://127.0.0.1:5000/drinks`
```
{
  "drinks": [
    {
      "id": 1,
      "recipe": [
        {
          "color": "blue",
          "parts": 1
        }
      ],
      "title": "water"
    }
  ],
  "success": true
}
```
#### GET /drinks-detail
- General:
    - Returns a success value, a list of available drinks with full description.
- Sample: `curl http://127.0.0.1:5000/drinks-detail -H "Authorization: Bearer JWT"`
```
{
  "drinks": [
    {
      "id": 1,
      "recipe": [
        {
          "color": "blue",
          "name": "water",
          "parts": 1
        }
      ],
      "title": "water"
    }
  ],
  "success": true
}
```
#### POST /drinks
- General:
    - Creates a drink using the submitted title and recipe. Returns success value and the drink's full description in json.
- Sample: `curl http://127.0.0.1:5000/drinks -X POST -H "Content-Type: application/json" -d '{"title":"Amazing", "recipe": [{"name": "ingre1", "color": "pink", "parts": 1}, {"name": "ingre2", "color": "red", "parts": 2}, {"name": "ingre3", "color": "purple", "parts": 1}]}' -H "Authorization: Bearer JWT"`
```
{
  "drinks": {
    "id": 2,
    "recipe": [
      {
        "color": "pink",
        "name": "ingre1",
        "parts": 1
      },
      {
        "color": "red",
        "name": "ingre2",
        "parts": 2
      },
      {
        "color": "purple",
        "name": "ingre3",
        "parts": 1
      }
    ],
    "title": "Amazing"
  },
  "success": true
}
```
#### PATCH /drinks/{drink_id}
- General:
    - Updates the drink of the given ID if it exists. Returns success value and the a list of drink's full description.
- Sample: `curl -X PATCH http://127.0.0.1:5000/drinks/2 -H "content-type: application/json" -d '{"title": "Special"}' -H "Authorization: Bearer JWT"`

```
{
  "drinks": [
    {
      "id": 2,
      "recipe": [
        {
          "color": "pink",
          "name": "ingre1",
          "parts": 1
        },
        {
          "color": "red",
          "name": "ingre2",
          "parts": 2
        },
        {
          "color": "purple",
          "name": "ingre3",
          "parts": 1
        }
      ],
      "title": "Special"
    }
  ],
  "success": true
}
```
#### DELETE /drinks/{drink_id}
- General:
    - Deletes the drink of the given ID if it exists. Returns the id of the deleted drink and success value.
- Sample: `curl -X DELETE http://127.0.0.1:5000/questions/1 -H "Authorization: Bearer JWT"`

```
{
  "delete": 1,
  "success": true
}
```

## Deployment N/A

## Authors
Ann Yang
