## Author
Jacob Rugano

### Description
This is a web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handymen to meeting announcements or even alerts.

### User Story
A user can:

1. Sign in with the application to start using.
2. Set up a profile with about me, a general location, and a neighborhood name.
3. Find a list of different businesses in their neighborhood.
4. Find Contact Information for the health department and Police authorities near their neighborhood.
5. Create posts that will be visible to everyone in their neighborhood.
6. Change their neighborhood when the user decides to move out.
7. Only view details of a single neighborhood.

### Getting Started
To set up the project in your local machine for development and testing:

1. Clone this Repository
2. git clone https://github.com/jacobrugano/neighborhoodIP4Django.git
3. Enable your Python development environment Add Python, pip and a virtual environment to get started:
4. python3.6 -m venv --without-pip virtual

5. $ source virtual/bin/activate

6. (virtual) $ curl https://bootstrap.pypa.io/get-pip.py | python

### Prerequisites
Install all project requirements using the package manager pip.

(virtual) $ pip install -r requirements.txt

#### Installation
Use the .env.example file to create a .env file with appropriate values to get a development env running.

Create a postgres db and add the credentials to .env file

Apply initial migrations

(virtual) $ python manage.py migrate

Create admin account

(virtual) $ python manage.py createsuperuser

Make migrations to your database

(virtual) $ python manage.py makemigrations (app name)

(virtual) $ python manage.py migrate

Start development server

(virtual) $ python3 manage.py runserver

#### Running Tests
To run automated tests for the system:

(virtual) $ python3 manage.py test (app name)

#### Deployment
With all environment variables changed to suit your local copy of this repository, deploy the application to Heroku to see it live or simply run it locally

(virtual) $ python3 manage.py runserver

#### Technology Used
Django 3.0.8 - The web framework used
Heroku - Deployment platform
Python3 - Backend logic
Postresql - Database system
Known Bugs
There are no known bugs currently but pull requests are allowed incase you spot a bug

#### Contact Information
If you have any question or contributions, please email: jerushaotienocoding@gmail.com

#### License
MIT License

##### Copyright
Copyright (c) 2022 Jacob Rugano