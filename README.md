# django-example

This is an example [Django](https://www.djangoproject.com) backend project with a complete authentication (standard auth, social auth (Google etc.)) using [allauth](https://docs.allauth.org/en/latest/). It is composed of two parts:
- a headless API that can be interfaced with any separated frontend (e.g [this next.js example project](https://github.com/Harold-Kalvin/nextjs-example))
- a monolithic solution with an integrated frontend that uses django's default template system and [htmx](https://htmx.org)

## Prerequisites
- [Docker](https://www.docker.com)

## Installation
To run the services, run:
```
docker compose up
```

The backend will be available at `http://localhost:8000` (The swagger page at: `http://localhost:8000/api/docs`).



