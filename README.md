# EduBlog-API-
EduBlog API is a FastAPI-powered backend service designed to support school and educational blogs. This API allows users to create, read, update, and delete blog posts, making it easy to share educational content, announcements, and news within a school or learning community. 

Features
CRUD Operations: Create, Read, Update, and Delete blog posts.
Data Validation: Uses Pydantic for strong data validation.
Asynchronous Database Interaction: Built on Motor (MongoDB Async Driver) for efficient asynchronous operations.
Dockerized Setup: Easy setup and deployment with Docker.
RESTful API: Follows REST principles, making it easy to integrate with other frontend applications.
Technologies Used
FastAPI: For creating the API endpoints.
MongoDB (Motor): Asynchronous MongoDB driver for Python.
Pydantic: For data validation.
Docker: Containerization of the application for easy deployment.
Getting Started
Prerequisites
Ensure you have the following installed:

Python 3.8+
MongoDB server or MongoDB Atlas account (cloud MongoDB service)
Docker (for deployment)


Installation
Clone the repository:
```
git clone https://github.com/AyaanShaheer/EduBlog-API-.git
cd edu-blog-api
```
Install dependencies:
```
pip install -r requirements.txt

```
Set up MongoDB connection:

* Configure your MongoDB URI. You can use a .env file to store your database connection URI.

* Create a file named .env in the project root and add:
```
MONGODB_URI="your_mongodb_uri"
```
Run the application:
```
uvicorn main:app --reload
```
Access the API documentation:
pen your browser and go to http://127.0.0.1:8000/docs to access the interactive API documentation provided by Swagger UI.

Docker Setup
Build the Docker image:
```
docker build -t edu-blog-api .
```
Run the Docker container:
```
docker run -d -p 8000:8000 --name edu-blog-api-container edu-blog-api
```
Verify the container is running:
Visit http://127.0.0.1:8000/docs to access the API documentation in your Dockerized application.

API Endpoints
Method	Endpoint	                       Description
GET	     /posts	                      Retrieve all blog posts
GET	     /posts/{id}	                Retrieve a blog post by ID
POST	   /posts	                      Create a new blog post
PUT	     /posts/{id}	                Update an existing blog post
DELETE	 /posts/{id}	                Delete a blog post by ID
