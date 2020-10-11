# Django+Vue Training Project

This repo contains code for my training project in Vue.js and Django. I'm familiar with both technologies, but never wrote a end-to-end project using both of them, myself.

## Tech stack

* Python, Django
* JS, Vue, Nuxt
* REST API
* Bulma
* Django Admin
* GitHub
* Heroku

## Usage

### Pre-requisites

* Python >= 3.8.2
* Pipenv 2020.8.13
* NodeJS >= 14.8.0
* Yarn >= 1.22.4

### Install

Install dependencies:

    make install

### Migrations

Create Django migrations like this:

    make migrations

And apply them:

    make migrate

### Run

Run Django app in dev mode:

    make run_backend

Run Nuxt app in dev mode:

    make run_frontend