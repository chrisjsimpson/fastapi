# Example FastAPI tutorial with automated deployment

Step-by-step tutorial: https://blog.karmacomputing.co.uk/fastapi-production-deployment-with-dokku-and-github-actions/

Built upon the *amazing* documentation at: https://fastapi.tiangolo.com/tutorial/
and thanks to https://github.com/idoberko2/dokku-deploy-github-action

## What do I get?

- Automated FastAPI deployments from the main branch using Dokku via Github actions

## How long will it take?

- About 30mins

## How much will it cost me?

- Your time, and about $5p/m if you don't already have a server

## How do I run it locally?

Create & activate a python3 [virtual environment](https://docs.python.org/3/tutorial/venv.html) (optional, but **very** recommended)

Install requirements:

```
pip install -r requirements.txt
```

Run the app locally:

```
cd app
uvicorn main:app --reload
```

Visit: 

```
http://127.0.0.1:8000
```

Port already in use? Close the other app, or use a difference port:

```
uvicorn main:app --port 8001 --reload 
```

How do I run this? 
uvicorn main:app --reload
