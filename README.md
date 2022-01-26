# Setup(root)

- create .env in project root

## Setup (frontend)

- create .env in /frontend/
- $ cd frontend
- $ npm install

## Setup (backend)

- $ cd backend
- $ source .venv/bin/activate
- $ cd backend
- $ pip isntall -r requirements.txt
- create .env in /backend/

## Start

### Start backend server on local host on port:8000

- cd backend
- python manage.py runserver

### Start backend server on local host on port:3000

- cd frontend
- npm run local

## Start (docker)

### Start the development server on http://localhost:5013

- cd project root directory
- $ docker-compose up --build

## typecheck (frontend)

- cd frontend
- $ npm run type
