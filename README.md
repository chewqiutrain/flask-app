## To run
Start Celery worker 
```bash
celery -A <filename containing celery tasks> -l INFO 
```

Then start Flask App 
```bash
python main.py
```
or 
```
flask run
```

Test endpoint
```
curl http://localhost:5000/do-slow
```
