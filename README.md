# Intail Assignment

## Overview

QuoteMaster is a full-stack application that displays famous quotes for users to read and interact with.
It was built with **ReactJs**, **FastAPI**, **PostgreSQL**, **Redis**, and **Docker**. 

## Architecture

[Frontend]:
  1. Requests quotes from the backend
  2. Requests author info from the backend
  3. Renders quotes with pagination and infinite scroll functionality
[Backend]:
  1. Runs a background task (hourly) for scraping quotes, using FastAPI's built-in task-scheduler, which calls a service to fetch the quote's author information from another 3rd party source.
  2. Saves Quote, Author and Book data to the db, and author data to the Redis Cache. This way the user has the fastest response time when clicking the "enhance button", all while 
  retaining the ability to persist data and decouple from the 3rd party source we initially rely on for gathering our data. Should they ever have issues, we will have all of our required information in our db.

## Setup

- [Clone]: git@github.com:ItaySagy12345/intail-assignment.git
- [Env]: Make .env files, one in app dir of the frontend and one in the server dir of the backend, with the env data I sent you by email, respectively.
- [Frontend]: Create your node_modules and package-lock.json: Run "make init1". To remove the node_modules, run "make destroy1", if needed
- [Backend]: Create your python venv: Run "make init2". To remove the venv, run "make destroy2", if needed
- [Backend]: Navigate to server/src/server.py and on line 20 change the "seconds=1 * 60 * 60" to 1, so that you can start scraping right after running the server locally for the first time.

<!-- For all Make commands, run from the root project dir -->
- [Frontend]: Start the react app: run "make app". 
- [Docker]: Build the necessary docker images: run "make build", then "make up". Run "make down" to shut your docker container down when you're done using the app.
- [Redis]: Start Redis: run "make redis".  
- [Backend]: Start the FastAPI server: run "make server" or if using vscode and you want to debug, just use the .vscode/launch.json provided

## Prerequisites

- Download node, pip if you don't have them already
- Download Redis: https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-mac-os/
- Download Docker Desktop: https://www.docker.com/products/docker-desktop/

## Testing

- [Frontend]: http://localhost:5173 : app GUI
- [Backend]: http://localhost:8000/docs : FastAPI Swagger GUI
- [Database]: http://localhost:8080 : Pgadmin GUI
- [Docker]: Docker Desktop to check logs in running container/services