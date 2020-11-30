# LaunchPad
This is an example application that consumes the [SpaceX API](https://github.com/r-spacex/SpaceX-API) and makes the data available via matching endpoints.

## Setup
With `docker-compose` local environment setup is as easy as `docker-compose up --build`. This creates a PostGres container and an application container, initializing both.

### Database
For the initial build of the PostGres database you will need to log into the application container `docker container exec -it launchpad-api sh` and execute `python manage.py makemigrations launchpads` and `python manage.py migrate`. This creates the migration files and the subsequent command creates the tables in the database on `launchpad-db`.

## Testing
Testing the application is simple: `python manage.py test`.
**Keep in mind that if you execute tests locally, outside of a docker container, you will need to change the .env file's POSTGRES_HOST value to localhost or 127.0.0.1** 