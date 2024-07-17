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

## Initial Data

The initial quiz is provided via a data migration. You can see the quiz via the admin panel or the sqlite database.

## Unimplemented functionality

I implemented the web app allowing the admin to create a "quiz", including a sample quiz with some questions. I was unable to implement the second portion that would mimic a user taking the quiz in time. There is essentially some broken code and logic for that using the `QuizResponse` and `QuestionResponse` models, the corresponding forms and the `create_response` view.



