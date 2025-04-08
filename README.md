# Recipe-App API

![alt text](https://github.com/kayprogrammer/socialnet-v1/blob/main/display/drf.png?raw=true)


## Description
The Recipe-App API powers a recipe management application. It allows users to manage recipes, ingredients, tags, and user profiles. The API supports Docker-based setup, GitHub Actions for CI/CD, and includes endpoints for user management, image uploads, and more. It also includes comprehensive unit tests to ensure reliability.

## Features

* User authentication and management
* Recipe management (CRUD operations)
* Ingredient management (CRUD operations)
* Tag management (CRUD operations)
* Image upload for recipes
* Comprehensive unit testing

## Installation
To get started with the Recipe-App API, you can clone the repository and follow the installation steps below.

#### Clone the Repository
* Clone the repository to your local machine:
```bash
    $ git clone https://github.com/iam-madukapaul/recipe-app-api.git
    $ cd recipe-app-api
```

## Docker Setup
The project supports Docker for easy setup and development. Follow the steps below to run the project using Docker.

#### 1. Build the Docker Image
* Make sure you have Docker installed on your system.
* In the root of the repository, build the Docker image:
```bash
    $ docker-compose build
```
#### 2. Make database migrations
* After building the Docker images, you should create any necessary database migrations for the application:
```bash
    $ docker-compose run --rm app sh -c "python manage.py makemigrations"
```

#### 3. Run the Application with Docker Compose
* To start the application, run the following command:
```bash
    $ docker-compose up
```
* The application will now be available at http://127.0.0.1:8000

## Testing
The project includes unit tests to ensure the API is functioning as expected.

#### Run Tests with Docker
* To run the tests inside the Docker container, use the following command:
```bash
    $ docker-compose run --rm app sh -c "python manage.py test"
```

## CI/CD Integration
This project is integrated with GitHub Actions for Continuous Integration and Continuous Deployment (CI/CD). The GitHub Actions workflow will run automatically on every push to the repository, ensuring that the API is tested, built, and deployed without manual intervention.

## Contributing
Contributions are welcome! If you'd like to contribute to the Recipe-App API, please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-name).
3. Make your changes.
4. Commit your changes (git commit -am 'Add new feature').
5. Push to the branch (git push origin feature-name).
6. Create a new pull request.

## Deployment
At the time of development, this project was deployed on AWS. As such, there are some AWS-specific deployment configurations within the code to support cloud deployment.

Please note that the deployment setup may need to be adjusted based on your environment, but this project was originally designed with AWS in mind.
![Screenshot 2025-04-08 082246](https://github.com/user-attachments/assets/0f353b0e-764b-487a-b293-9fbabb21edf1)
