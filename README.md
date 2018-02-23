

# INSTALL DOCKER COMPOSE

    Build and start the app:

        docker-compose up
        # Or to rebuild
        docker-compose up --build

    Other helpful commands

        # enter db
        docker-compose run db psql -U postgres

        # enter bash shell
        docker-compose run app /bin/bash

        # stop everything
        docker-compose stop

        # stop everything, destroy containers, and volumes
        docker-compose down

    Override the default docker compose variables

        # vim docker-compose.override.yml
        version: '3.4'
        services:
            app:
              ports:
                - 8001:8000
