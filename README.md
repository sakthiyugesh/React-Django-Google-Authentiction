## Google Authentication with React and Django Using Json Wen Tokens.
This project implements user authentication using JSON Web Tokens (JWT) with a React front-end and a Django back-end.

## Features
- **User Registration**: New users can sign up with their credentials.

- **User Login**: Users can log in to get a JWT token.

- **JWT** Authentication: Protected routes and API endpoints using JWT.

- **Token Refresh**: Supports refreshing JWT tokens to keep the user authenticated.

- **secure Routes**: Front-end routes are secured based on authentication status
- 
## Install (method 1 ):Reccomended!

Creating Virtual Environment:

```sh
$ python -m venv env
$ source env/bin/activate
```
Django Setup:

```sh
$ cd google_auth
$ pip install requirements.txt
```
React + Vite  Setup:
```sh
$ cd frontend
$ npm install 
```
## Usage
```sh
$ cd frontend
$ npm run dev

```
```sh
$ cd backend
$ py manage.py createsuperuser
$ py manage.py runserver
```

## **Method 2 - using Docker**
**usage**
```sh
$ cd backend
$ py manage.py createsuperuser
$ cd ..
$ docker-compose up --build
```

If this project helped you, please ⭐ the repository and follow for more updates..!

