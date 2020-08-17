# Example FastAPI tutorial with automated deployment

Tutorial: https://blog.karmacomputing.co.uk/fastapi-production-deployment-with-dokku-and-github-actions/

Built upon the *amazing* documentation at: https://fastapi.tiangolo.com/tutorial/

## How do I run it locally?

Create & activate a python3 [virtual environment](https://docs.python.org/3/tutorial/venv.html) (optional, but **very** recommended)

Install requirements:

```
pip install -r requirements.txt

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
