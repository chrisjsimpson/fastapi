# Example FastAPI tutorial with automated deployment

Step-by-step tutorial: https://blog.karmacomputing.co.uk/fastapi-production-deployment-with-dokku-and-github-actions/

Built upon the *amazing* documentation at: https://fastapi.tiangolo.com/tutorial/
and thanks to https://github.com/idoberko2/dokku-deploy-github-action

## What do I get?

- Automated FastAPI deployments from the main branch using Dokku via Github actions
- Automated TLS certificates and renewal
- Automated OpenAPI docs thanks to FastAPI [Demo](https://api.pcpink.co.uk/docs)

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

Manually seed the database (not needed because using `create_all` in `main.py`, but useful to know how to access the db without 
booting the entire app):

```
python
Python 3.6.8 (default, Apr  9 2019, 04:59:38) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from app import models
>>> from app.database import engine
>>> models.Base.metadata.create_all(bind=engine)
>>> exit()
```

Verify the database by looking for `sql_app.db` in your project root directory. Then using `sqlite3` to verify the schema e.g.:

```
sqlite3 sql_app.db
SQLite version 3.24.0 2018-06-04 19:24:41
Enter ".help" for usage hints.
sqlite> .schema
CREATE TABLE users (
	id INTEGER NOT NULL, 
  ...
);
CREATE UNIQUE INDEX ix_users_email ON users (email);
CREATE INDEX ix_users_id ON users (id);
CREATE TABLE items (
	id INTEGER NOT NULL, 
  ...
);
CREATE INDEX ix_items_title ON items (title);
...
sqlite> .q
```

Manually access the database:

```
sqlite3 sql_app.db
SQLite version 3.24.0 2018-06-04 19:24:41
Enter ".help" for usage hints.
>>> from app.database import *
>>> db = SessionLocal()
>>> from app.models import User
>>> db.query(User).all()
>>> [] # Empty
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

## Performance

Pointless benchmark: Throwing 10,000's request, with concurrency 10 at
the /random endpoint which generates and returns a pseudo random number using
python's `random` function, served by FastAPI.

Instance: Cheap as chips $5 VPS with 1024MB Memory, 1000GB Bandwidth, running 
ubuntu 18.04 with only 129M of free memory (`free -h`).

A median of 62ms for `processing` and `waiting seems` pretty good. [see definitions](https://stackoverflow.com/questions/2820306/definition-of-connect-processing-waiting-in-apache-bench).

```
$ ab -n 10000 -c 100 https://api.pcpink.co.uk/random
This is ApacheBench, Version 2.3 <$Revision: 1826891 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking api.pcpink.co.uk (be patient)
Completed 1000 requests
Completed 2000 requests
Completed 3000 requests
Completed 4000 requests
Completed 5000 requests
Completed 6000 requests
Completed 7000 requests
Completed 8000 requests
Completed 9000 requests
Completed 10000 requests
Finished 10000 requests


Server Software:        nginx
Server Hostname:        api.pcpink.co.uk
Server Port:            443
SSL/TLS Protocol:       TLSv1.2,ECDHE-RSA-AES256-GCM-SHA384,4096,256
TLS Server Name:        api.pcpink.co.uk

Document Path:          /random
Document Length:        36 bytes

Concurrency Level:      100
Time taken for tests:   128.593 seconds
Complete requests:      10000
Failed requests:        3978
   (Connect: 0, Receive: 0, Length: 3978, Exceptions: 0)
Total transferred:      2422812 bytes
HTML transferred:       362812 bytes
Requests per second:    77.76 [#/sec] (mean)
Time per request:       1285.932 [ms] (mean)
Time per request:       12.859 [ms] (mean, across all concurrent requests)
Transfer rate:          18.40 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:       56 1217  78.6   1215    2251
Processing:    31   62  11.6     62     333
Waiting:       16   62  11.4     62     332
Total:         87 1279  80.2   1277    2526

Percentage of the requests served within a certain time (ms)
  50%   1277
  66%   1287
  75%   1294
  80%   1298
  90%   1315
  95%   1339
  98%   1400
  99%   1464
 100%   2526 (longest request)
```
