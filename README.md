# job-management-portal

# Instalation

- Clone the repository;
- Go to the projects local folder;
- Start a virtual environment: `virtualenv -p python3.11 venv`;
- Activate venv `source venv/bin/activate`;
- Install Poetry lib manager: `pip install poetry`;
- Install libs: `poetry install`
- Run the migrations: `python manage.py migrate`;
- Create a superuser: `python manage.py createsuperuser`;
- Run the server: `python manage.py runserver`.