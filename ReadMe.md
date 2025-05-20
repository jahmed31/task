# Task App

Task App is a Django-based project designed to manage tasks.

## Key Technologies Used
- **Python3.11**: python version.
- **Django**: python version.
- **Django-Restframework**: For writing APIs.
- **Django-Pytest**: For writing tests.
- **Django Authetentication**: For RestAPI authentication.
- **Swagger**: For documenting API endpoints.
- **PostgreSQL**: For database.
- **nginx**: Reverse proxy server is nginx.
- **Docker**: Docker and docker-compose been used for building and running services.
- **tailwindcss**: CDN for tailwind used and attached in `base.html`

## Getting Started
Docker compose file `docker-compose.yml` available in which services has been defined
1. `web`
2. `database`
3. `nginx`

My strategy to make the code simple and clean. 

### Installation and details 

1. **Clone the repository**:
   ```sh
   git clone <url>   
   ```
2. **Project Structure**: <br />
   The directory **smart_nsales** where you can find all main files related to the project
   _nginx configuration_ folder, _docker-compose.yml_, _dokcerfile_, _requirements.txt_ and _wait_for_db.sh_ files which
   are part of the project. The project where django application is `smart` folder where three app folder 
   defined, `app` for django `CRUD` and `api` for REST API `CRUD`, Few tests been written for django and 
   django-restframework which are in each in the applications folders of `app` and `api` files `test.py`.
   Application used `custom user` model for django application, Can be found in `users` directory.
    
3. **Running Project**:<br />
   Change directory to smart_nsales project and run with docker compose 
    ```sh
   cd smart_nsales
   docker-compose build --no-cache && docker-compose up --force-recreate
   ```
   Make sure to create superuser to start using admin and creating users from admin. <br />
   ```docker exec -it smart_nsales_web_1 python manage.py createsuperuser```  <br />
   Project can be access over `http://localhost:8080` <br />
   Project admin access URL is `http://localhost:8080/admin/` <br />
   Project sign-in URL is `http://localhost:8080/users/login/` <br />
   <br />

4.  **Documentation**: <br />
    To access documentation endpoint for RestAPI `http://localhost:8080/redoc/` where you can observe all 
    endpoints. <br /> 
    <br />

5. **POSTMAN**: <br />
   Postman collection has been attached for testing API end points. In `login` postman collection
   i have written a write code in `TEST` section to dynamically save token and used in the collection. Make sure to set 
   your environment variable are set accordingly. <br />


6. **pytest**:
   To run all tests use the following command 
   ```sh
   docker exec -it smart_nsales_web_1 pytest
   ```
   `test.py` available in both `app` and `api` folders. <br />


7. **Comments**:
   In `views.py` files you can see all the views related to django and django restframework `app` and `api`.
   Try to follows pep8 standard for commenting each function. 