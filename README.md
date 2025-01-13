
# Django API Test

## Overview

This project is a test API built with Django. It provides endpoints for performing basic operations on tasks and managing users, including authentication.

## Running the Application

To start the application go to the app folder and write the command : ` docker-compose up --build`

## Authentication

The API uses JWT (JSON Web Tokens) for authentication. To access protected routes, include the token in the `Authorization` header with the `Bearer` scheme.

## Task Operations

### Retrieve a Task

- **URL:** `/task/{id}/`
- **Method:** `GET`
- **Description:** Retrieves a specific task by its ID. 
- **Parameters:**
  - `id` (path) - ID of the task to retrieve (integer).
- **Responses:**
  - `200 OK` - The task was retrieved successfully.
  - `404 Not Found` - The requested task does not exist.
  - `401 Unauthorized` - Authentication credentials were not provided or are invalid.

### Update a Task

- **URL:** `/task/{id}/`
- **Method:** `PUT`
- **Description:** Updates a specific task. The task is identified by its ID, and the request body must contain the updated task data.
- **Parameters:**
  - `id` (path) - ID of the task to update (integer).
- **Request Body:** Must include updated task data.
- **Responses:**
  - `200 OK` - The task was updated successfully.
  - `400 Bad Request` - Invalid data was provided for the update operation.
  - `404 Not Found` - The requested task does not exist.
  - `401 Unauthorized` - Authentication credentials were not provided or are invalid.

### Partially Update a Task

- **URL:** `/task/{id}/`
- **Method:** `PATCH`
- **Description:** Partially updates a specific task. The task is identified by its ID, and the request body may contain only the fields to be updated.
- **Parameters:**
  - `id` (path) - ID of the task to partially update (integer).
- **Request Body:** Must include updated fields.
- **Responses:**
  - `200 OK` - The task was partially updated successfully.
  - `400 Bad Request` - Invalid data was provided for the update operation.
  - `404 Not Found` - The requested task does not exist.
  - `401 Unauthorized` - Authentication credentials were not provided or are invalid.

### Delete a Task

- **URL:** `/task/{id}/`
- **Method:** `DELETE`
- **Description:** Deletes a specific task by its ID.
- **Parameters:**
  - `id` (path) - ID of the task to delete (integer).
- **Responses:**
  - `204 No Content` - The task was deleted successfully.
  - `404 Not Found` - The requested task does not exist.
  - `401 Unauthorized` - Authentication credentials were not provided or are invalid.

### Create a New Task

- **URL:** `/task/create/`
- **Method:** `POST`
- **Description:** Creates a new task. The request body must contain all required fields.
- **Request Body:** Must include all required fields.
- **Responses:**
  - `201 Created` - The task was created successfully.
  - `400 Bad Request` - The request body is invalid or missing required fields.

### List All Tasks

- **URL:** `/task/list/`
- **Method:** `GET`
- **Description:** Retrieves a list of all tasks. The response can be filtered using query parameters.
- **Parameters:**
  - `assigned_to_user` (query) - Filter tasks assigned to the currently authenticated user. Set to `true` to filter tasks assigned to the user.
  - `page` (query) - A page number within the paginated result set (integer).
- **Responses:**
  - `200 OK` - A list of tasks.
  - `401 Unauthorized` - Authentication credentials were not provided or are invalid.

## User Operations

### Login

- **URL:** `/user/login/`
- **Method:** `POST`
- **Description:** Takes a set of user credentials and returns an access and refresh JSON web token pair to prove the authentication of those credentials.
- **Request Body:** Must include user email and password.
- **Responses:**
  - `200 OK` - Access and refresh tokens.

### Refresh Token

- **URL:** `/user/login/refresh/`
- **Method:** `POST`
- **Description:** Takes a refresh token and returns an access token if the refresh token is valid.
- **Request Body:** Must include a refresh token.
- **Responses:**
  - `200 OK` - Access and refresh tokens.

### Logout

- **URL:** `/user/logout/`
- **Method:** `POST`
- **Description:** Takes a token and blacklists it. Requires `rest_framework_simplejwt.token_blacklist` app installed.
- **Request Body:** Must include a refresh token.
- **Responses:**
  - `200 OK` - No response body.

### Register

- **URL:** `/user/register/`
- **Method:** `POST`
- **Description:** Allows anyone to register a new user. The request body must contain the required fields.
- **Request Body:** Must include email, username, and password.
- **Responses:**
  - `201 Created` - User registration was successful.
  - `400 Bad Request` - The request body is invalid or missing required fields.


## Security

- **JWT Authentication:** Include the JWT token in the `Authorization` header with the `Bearer` scheme.

## Swagger
- **Swagger UI:** You can access the Swagger UI for API documentation and testing at [http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/).