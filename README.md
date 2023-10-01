# image_upload_project
To setup the project follow by instruction below:

1. Create a virtual environment and activate it:
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate

2. Install the dependencies:
    pip install -r requirements.txt

3. Apply database migrations:
    python3 manage.py migrate

4. Create a superuser (admin):
    python manage.py createsuperuser

5. Run the development server:
    python3 manage.py server 8000