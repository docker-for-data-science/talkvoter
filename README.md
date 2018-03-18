# TalkVoter

## Todo

- [ ] Need better name
- [x] Add MakeFile
- [ ] Add API and DB documentation
- [ ] Create Backend
- [ ] Create Frontend

## Instructions

1. Install Docker
1. Clone repo

### Makefile Commands

```text
Makefile for managing web application

Usage:
 make build      build images
 make up         creates containers and starts service
 make start      starts service containers
 make stop       stops service containers
 make down       stops service and removes containers

 make migrate    run migrations
 make test       run tests
 make test_cov   run tests with coverage.py
 make test_fast  run tests without migrations
 make lint       run flake8 linter

 make attach     attach to process inside service
 make logs       see container logs
 make shell      connect to app container in new bash shell
 make dbshell    connect to postgres inside db container
```

## Overriding Default Docker-Compose Settings

Create a `docker-compose.override.yml` as follows:

```text
# docker-compose.override.yml
version: '3.4'
services:
  app:
    ports:
      - 8001:8000
```

[Additional information](https://docs.docker.com/compose/extends/).
