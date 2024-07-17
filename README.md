# Quiz App Interview

Tech Stack:
- Django
- SQLite


Given that this is timed to only 3 hours, and my role is backend focused: I decided to keep the tech stack simple to focus on implementing features and have ease-of-setup and use. So I am sticking with Django for both the backend  and to serve the frontend with templates. I'll also keep to function based views and simple models as much as possible. I chose SQLite instead of Postgres for similar reasons. I also expect to mostly use the Django ORM to interact with the database.


## Getting Started

Create a virtual environment if you like, and then the project can be initialized with:

```
cd webapp/
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
This will start the development server and you can access the application in your browser at `http://localhost:8000`.



